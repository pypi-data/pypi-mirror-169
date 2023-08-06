"""Time tracking."""

import logging
import os

import luigi
import pandas as pd
import trackpy as tp

from .config import General
from .config import SpotsDetection
from .config import SpotsTracking
from .detect import Detect

tp.quiet()


class Track(luigi.Task):
    """Join spots to tracks in a 2D+T image."""

    FileID = luigi.Parameter()
    ChannelIndex = luigi.IntParameter()
    logger = logging.getLogger("koopa")

    def requires(self):
        return Detect(FileID=self.FileID, ChannelIndex=self.ChannelIndex)

    def output(self):
        return luigi.LocalTarget(
            os.path.join(
                General().analysis_dir,
                f"detection_final_c{SpotsDetection().channels[self.ChannelIndex]}",
                f"{self.FileID}.parq",
            )
        )

    def run(self):
        df = pd.read_parquet(self.requires().output().path)
        df = self.track(df)
        df.to_parquet(self.output().path)

    def track(self, df: pd.DataFrame) -> pd.DataFrame:
        """Nearest neighbor based tracking."""
        track = tp.link_df(
            df,
            search_range=SpotsTracking().search_range,
            memory=SpotsTracking().gap_frames,
        )
        track = tp.filter_stubs(track, threshold=SpotsTracking().min_length)
        self.logger.info(f"Tracked {len(track)} spots.")

        if General().do_3D:
            self.logger.info(f"Linking 3D image {self.FileID}.")
            track = self.link_brightest_particles(df, track)

        if SpotsTracking().subtract_drift:
            self.logger.info(f"Subtracting drift from {self.FileID}.")
            track = self.subtract_drift(track)

        return self.clean_particles(track)

    @staticmethod
    def subtract_drift(df: pd.DataFrame) -> pd.DataFrame:
        drift = tp.compute_drift(df)
        df_clean = tp.subtract_drift(df.copy(), drift)
        return df_clean

    @staticmethod
    def clean_particles(df: pd.DataFrame) -> pd.DataFrame:
        df["particle"] = pd.factorize(df["particle"])[0]
        df = df.reset_index(drop=True)
        return df

    @staticmethod
    def link_brightest_particles(df: pd.DataFrame, track: pd.DataFrame) -> pd.DataFrame:
        # Index of brightest particles
        idx = track.groupby(["particle"])["mass"].transform(max) == track["mass"]
        df_nms = track[idx]

        # Remove the non-track particles
        df_without_track = df[
            ~df.set_index(["x", "y", "frame", "mass"]).index.isin(
                track.set_index(["x", "y", "frame", "mass"]).index
            )
        ]

        # Add back nms (brightest spots)
        df_clean = pd.concat([df_nms, df_without_track]).reset_index(drop=True)
        return df_clean
