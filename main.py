# Generic Packages
import numpy as np
import pandas as pd

# geospacial packages
import rasterio

# import landlab packages
from landlab import RasterModelGrid, imshow_grid
from landlab.components import (
    DepressionFinderAndRouter,
    FastscapeEroder,
    FlowAccumulator,
    LinearDiffuser,
    StreamPowerEroder,
)
# import matplotlib
# matplotlib.use('TkAgg')  # Cambiar a un backend interactivo
from matplotlib import pyplot as plt
from rasterio.plot import show


def describe_raster(filename):
    """Describe the raster file and print its metadata.

    Args:
        filename (str): The path to the raster file.
    """
    with rasterio.open(filename) as src:
        print("Profile: \n", src.profile)
        print("Size: \n", src.width, src.height)
        print("Bounds: \n", src.bounds)
        print("Coordinate Reference System: \n", src.crs)
        print("Transform: \n", src.transform)
        print("Data Type: \n", src.dtypes[0])
        print("No. of Bands: \n", src.count)
        print("No. of Pixels: \n", src.width * src.height)
        print("No. of NoData Values: \n", src.nodata)
        print("No. of Overviews: \n", src.overviews(1))
        print("Block Size: \n", src.block_shapes[0])
        print("Compression: \n", src.compression)
        print("Interleave: \n", src.interleaving)
        print("Driver: \n", src.driver)
        print("Tags: \n", src.tags())
        print("Tags (all): \n", src.tags(ns=None))
        print("Tags (ns): \n", src.tags(ns=""))

def describe_elevation(elevArr):
    """Describe the elevation array and print its metadata.

    Args:
        elevArr (numpy.ndarray): The elevation array.
    """
    print("Elevation Array: \n", elevArr)
    print("Shape: \n", elevArr.shape)
    print("Data Type: \n", elevArr.dtype)
    print("No. of NoData Values: \n", np.isnan(elevArr).sum())
    print("Min Value: \n", np.nanmin(elevArr))
    print("Max Value: \n", np.nanmax(elevArr))
    print("Mean Value: \n", np.nanmean(elevArr))
    print("Std Value: \n", np.nanstd(elevArr))

def createGridFromRaster(ncols: float, nrows: float, dxy: float, elevArr:np.ndarray = None):
    """Create a RasterModelGrid from the elevation array and metadata.

    Args:
        rasterObj (numpy.ndarray): The elevation data.
        metadata (dict): The metadata of the raster file.

    Returns:
        RasterModelGrid: A RasterModelGrid object created from the elevation array and metadata.
    """

    # define a landlab raster
    # create a landlab grid
    mg = RasterModelGrid(
        shape=(nrows, ncols),
        xy_spacing=dxy,
        # xy_of_lower_left=(rasterObj.bounds[0], rasterObj.bounds[1]),
        xy_of_lower_left=(0, 0),
    )
    print(nrows, ncols, dxy)
    # create dataset with zero values
    zr = mg.add_zeros("topographic__elevation", at="node")
    # add the elevation data to the grid
    if elevArr is not None:
        # convert the elevation array to a 1D array
        zr += elevArr[::-1,:].ravel()

        imshow_grid(mg, "topographic__elevation", shrink=0.5, at="node")
    return mg


def main():
    # Open the raster file and get the data and metadata
    filename = "./assets/rst/clippedDem_12N.tif"
    rasterObj = rasterio.open(filename)
    show(rasterObj)

    # describe_raster(filename)
    elevArr = rasterObj.read(1)  # <class 'numpy.ndarray'>
    describe_elevation(elevArr)
    meta = rasterObj.meta
    print(meta)
    show(elevArr, cmap="terrain")

    dxy = rasterObj.res  # side length of a raster model cell, or resolution [m], initially 50
    createGridFromRaster(rasterObj.width, rasterObj.height, dxy)


if __name__ == "__main__":
    main()
