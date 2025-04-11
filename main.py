# Generic Packages
import numpy as np
import pandas as pd

# geospacial packages
import rasterio
from matplotlib import pyplot as plt
from rasterio.plot import show

# import landlab packages
from landlab import RasterModelGrid, imshow_grid
from landlab.components import (
    
    FlowAccumulator,
    DepressionFinderAndRouter,
    FastscapeEroder,
    LinearDiffuser,
    StreamPowerEroder,
)

def describe_raster(filename):
    """Describe the raster file and print its metadata.

    Args:
        filename (str): The path to the raster file.
    """
    with rasterio.open(filename) as src:
        print("Profile: \n", src.profile)
        print("Size: \n",src.width, src.height)
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
        print("Tags (ns): \n", src.tags(ns=''))
        print(src.read(1))

def openRaster(filename):
    """Open a raster file and return the data and metadata.

    Args:
        filename (str): The path to the raster file.

    Returns:
        tuple: A tuple containing the data and metadata of the raster file.
    """
    with rasterio.open(filename) as src:
        show(src)
        data = src.read(1)
        meta = src.meta
    return data, meta

def createGridFromRaster(rasterObj, metadata):
    """Create a RasterModelGrid from the elevation array and metadata.

    Args:
        rasterObj (numpy.ndarray): The elevation data.
        metadata (dict): The metadata of the raster file.

    Returns:
        RasterModelGrid: A RasterModelGrid object created from the elevation array and metadata.
    """
    grid = RasterModelGrid((metadata['height'], metadata['width']), xy_spacing=(metadata['transform'][0], metadata['transform'][4]))
    grid.add_field('topographic__elevation', rasterObj, at='node')
    return grid


def main():
    # Open the raster file and get the data and metadata
    filename = './assets/rst/clippedDem_12N.tif'
    rasterObj = openRaster(filename)
    describe_raster(filename)
    elevArr = rasterObj[0] # <class 'numpy.ndarray'>
    meta = rasterObj[1] # <class 'dict'>
    show(elevArr, cmap='terrain')
    


if __name__ == "__main__":
    main()
