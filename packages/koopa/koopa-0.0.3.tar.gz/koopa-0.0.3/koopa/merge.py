"""Merge all tasks to summary."""

import logging
import multiprocessing
import os

import luigi
import numpy as np
import pandas as pd
import scipy.ndimage as ndi
import skimage.measure
import tifffile

from . import util
from .colocalize import ColocalizeFrame
from .colocalize import ColocalizeTrack
from .config import FlyBrainCells
from .config import General
from .config import SegmentationCells
from .config import SegmentationOther
from .config import SpotsColocalization
from .config import SpotsDetection
from .detect import Detect
from .segment_cells import SegmentCells
from .segment_cells_flies import DilateCells
from .segment_other import SegmentOther
from .track import Track


class Merge(luigi.Task):
    """Task to merge workflow tasks into a summary and initiate paralellization."""

    threads = luigi.IntParameter()
    logger = logging.getLogger("koopa")

    @property
    def file_list(self):
        """All file basenames in the image directory."""
        return util.get_file_list()

    def requires(self):
        required_inputs = {}

        for fname in self.file_list:
            required = {}

            # Segmentation Nuclei/Cyto/Both
            if FlyBrainCells().enabled:
                required["cells"] = DilateCells(FileID=fname)
            else:
                required["cells"] = SegmentCells(FileID=fname)

            # Segmentation Other
            if SegmentationOther().enabled:
                for idx, _ in enumerate(SegmentationOther().channels):
                    required[f"other_{idx}"] = SegmentOther(
                        FileID=fname, ChannelIndex=idx
                    )

            # Spots detection
            for idx, _ in enumerate(SpotsDetection().channels):
                required[f"detect_{idx}"] = Detect(FileID=fname, ChannelIndex=idx)
                if General().do_3D or General().do_TimeSeries:
                    required[f"track_{idx}"] = Track(FileID=fname, ChannelIndex=idx)

            # Colocalization
            if SpotsColocalization().enabled:
                for idx, _ in enumerate(SpotsColocalization().channels):
                    required[f"colocalize_{idx}"] = (
                        ColocalizeTrack(FileID=fname, ChannelPairIndex=idx)
                        if General().do_TimeSeries
                        else ColocalizeFrame(FileID=fname, ChannelPairIndex=idx)
                    )

            required_inputs[fname] = required

        return required_inputs

    def output(self):
        return luigi.LocalTarget(os.path.join(General().analysis_dir, "summary.csv"))

    def run(self):
        """Merge all analysis files into a single summary file."""
        with multiprocessing.Pool(self.threads) as pool:
            dfs = pool.map(self.merge_file, self.file_list)
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv(self.output().path, index=False)

    def read_spots_file(self, file_id: str) -> pd.DataFrame:
        """Read the last important spot files dependent on selected config."""
        if SpotsColocalization().enabled:
            dfs = [
                pd.read_parquet(
                    self.requires()[file_id][f"colocalize_{idx}"].output().path
                )
                for idx, _ in enumerate(SpotsColocalization().channels)
            ]
        elif General().do_3D or General().do_TimeSeries:
            dfs = [
                pd.read_parquet(self.requires()[file_id][f"track_{idx}"].output().path)
                for idx, _ in enumerate(SpotsDetection().channels)
            ]
        else:
            dfs = [
                pd.read_parquet(self.requires()[file_id][f"detect_{idx}"].output().path)
                for idx, _ in enumerate(SpotsDetection().channels)
            ]
        return pd.concat(dfs, ignore_index=True)

    def get_value(self, row: pd.Series, image: np.ndarray) -> int:
        """Get pixel intensity from coordinate value."""
        if image.ndim == 3:
            return image[
                int(row["frame"]),
                min(int(row["y"]), image.shape[1] - 1),
                min(int(row["x"]), image.shape[2] - 1),
            ]
        if image.ndim == 2:
            return image[
                min(int(row["y"]), image.shape[0] - 1),
                min(int(row["x"]), image.shape[1] - 1),
            ]
        raise ValueError(f"Segmentation image must be 2D or 3D. Got {image.ndim}D.")

    @staticmethod
    def get_distance_from_segmap(
        df: pd.DataFrame, segmap: np.ndarray, identifier: str
    ) -> list:
        """Measure the distance of the spot to the periphery of a segmap."""
        distances = []
        for cell_id, dfg in df.groupby(identifier):
            mask = segmap == cell_id
            erosion = ndi.binary_erosion(mask)
            arr1 = np.array(np.where(np.bitwise_xor(erosion, mask))).T
            arr2 = dfg[["y", "x"]].values
            rmsd = np.mean(np.sqrt((arr1[None, :] - arr2[:, None]) ** 2), axis=2)
            distances.extend(np.min(rmsd, axis=1))
        return distances

    def get_cell_properties(self, segmap: np.ndarray, name: str) -> pd.DataFrame:
        """Find common measurements using regionprops."""
        properties = ["label", "area"]
        if not General().do_3D:
            properties.append("eccentricity")
        props = skimage.measure.regionprops_table(segmap, properties=properties)
        df = pd.DataFrame(props)
        df.columns = ["cell_id", *(f"{prop}_{name}" for prop in properties[1:])]
        return df

    def merge_file(self, file_id: str):
        """Merge all components of a single file `file_id`."""
        self.logger.info(f"Processing file - {file_id}")
        df = self.read_spots_file(file_id)

        # Cellular segmentation
        for selection in ("cyto", "nuclei"):
            if SegmentationCells().selection in (selection, "both"):
                image = tifffile.imread(
                    self.requires()[file_id]["cells"].output()[selection].path
                )
                df_cell = self.get_cell_properties(image, selection)
                df["cell_id"] = df.apply(lambda row: self.get_value(row, image), axis=1)
                df = pd.merge(df, df_cell, on="cell_id")
        df["num_cells"] = len(np.unique(image)) - 1

        if SegmentationCells().selection == "both":
            df["nuclear"] = df.apply(
                lambda row: bool(self.get_value(row, image)), axis=1
            )

        # Border distance
        # if SegmentationSecondary().border_distance:
        #     df["distance_from_secondary"] = self.get_distance_from_segmap(
        #         df, secondary, "secondary"
        #     )

        # Other segmentation
        if SegmentationOther().enabled:
            for idx, _ in enumerate(SegmentationOther().channels):
                other = tifffile.imread(
                    self.requires()[file_id][f"other_{idx}"].output().path
                )
                df[f"other_{idx}"] = df.apply(
                    lambda row: self.get_value(row, other), axis=1
                ).astype(bool)

        return df
