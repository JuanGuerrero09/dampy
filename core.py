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
    DepressionFinderAndRouter,
    FlowAccumulator,
    LinearDiffuser,
    StreamPowerEroder,
)
# import matplotlib
# matplotlib.use('TkAgg')  # Cambiar a un backend interactivo
from matplotlib import pyplot as plt
from rasterio.plot import show

def describeRaster(rasterObj: rasterio.io.DatasetReader):
    """Describe the raster object and print its metadata.

    Args:
        rasterObj (rasterio.io.DatasetReader): The raster object.
    """
    print("Profile: \n", rasterObj.profile)
    print("Shape: \n", rasterObj.shape) # shape of the raster (height, width) -> (rows, cols)
    print("Size (in pixels): \n", rasterObj.width * rasterObj.height) # size of the raster in pixels
    print("Number of Rows: \n", rasterObj.height) # number of rows in the raster
    print("Number of Columns: \n", rasterObj.width) # number of columns in the raster
    print("Bounds: \n", rasterObj.bounds) # bounds of the raster (left, bottom, right, top)
    print("Coordinate Reference System: \n", rasterObj.crs) # coordinate reference system
    print("Transform: \n", rasterObj.transform) # affine transformation matrix
    print("Resolution: \n", rasterObj.res) # resolution of the raster (x, y) -> also dxy
    print("Data Type: \n", rasterObj.dtypes[0]) # data type of the raster
    print("No. of Bands: \n", rasterObj.count) # number of bands
    print("No. of Pixels: \n", rasterObj.width * rasterObj.height) # number of pixels
    print("No. of NoData Values: \n", rasterObj.nodata) # number of missing values
    print("No. of Overviews: \n", rasterObj.overviews(1)) # number of overviews
    print("Block Size: \n", rasterObj.block_shapes[0]) # block size of the raster
    print("Compression: \n", rasterObj.compression) # compression type
    print("Interleave: \n", rasterObj.interleaving) # interleave type
    print("Driver: \n", rasterObj.driver) # driver type
    print("Tags: \n", rasterObj.tags()) # tags of the raster
    print("Tags (all): \n", rasterObj.tags(ns=None)) # tags of the raster with all namespaces
    print("Tags (ns): \n", rasterObj.tags(ns="")) # tags of the raster with a specific namespace



def describe_elevation(elevArr):
    """Describe the elevation array and print its metadata.

    Args:
        elevArr (numpy.ndarray): The elevation array.
    """
    print("Elevation Array: \n", elevArr) # elevation array
    print("Shape: \n", elevArr.shape) # shape of the elevation array (rows, cols)
    print("Data Type: \n", elevArr.dtype) # data type of the elevation array
    print("No. of NoData Values: \n", np.isnan(elevArr).sum()) # number of missing values
    print("Min Value: \n", np.nanmin(elevArr)) # minimum value of the elevation array
    print("Max Value: \n", np.nanmax(elevArr)) # maximum value of the elevation array
    print("Mean Value: \n", np.nanmean(elevArr)) # mean value of the elevation array
    print("Std Value: \n", np.nanstd(elevArr)) # standard deviation of the elevation array


def CreateGridFromDEM(rasterObj: rasterio.io.DatasetReader, add_elev: bool = False) -> RasterModelGrid:
    """Create a RasterModelGrid from the raster object.

    Args:
        rasterObj (rasterio.io.DatasetReader): The raster object.
        add_elev (bool, optional): Whether to add elevation data to the grid. Defaults to False.

    Returns:
        RasterModelGrid: A RasterModelGrid object created from the raster object.
    """
    # Get the metadata from the raster object
    ncols = rasterObj.width
    nrows = rasterObj.height
    dxy = rasterObj.res[0]

    # Create a RasterModelGrid from the raster object
    mg = RasterModelGrid(
        shape=(nrows, ncols),
        xy_spacing=dxy,
        xy_of_lower_left=(rasterObj.bounds[0], rasterObj.bounds[1]),
    )
    if add_elev:
        # Create a dataset with zero values
        zr = mg.add_zeros("topographic__elevation", at="node")
        # Add the elevation data to the grid
        elevArr = rasterObj.read(1)
        # Convert the elevation array to a 1D array
        zr += elevArr[::-1, :].ravel()
        
        #clear empty values
        #TODO Check if is actually needed
        mg.set_nodata_nodes_to_closed(zr, -9999)
        
        # Show the grid with the elevation data (only shows if is an interactive backend)
        imshow_grid(mg, "topographic__elevation", shrink=0.5, at="node")
    return mg

def getRasterObject(filename: str) -> rasterio.io.DatasetReader:
    """Get the raster object from the file.

    Args:
        filename (str): The path to the raster file.

    Returns:
        rasterio.io.DatasetReader: The raster object.
    """
    return rasterio.open(filename)

def define_basin_from_coords(mg: RasterModelGrid, coords: tuple) -> np.ndarray:
    """Define a basin mask from given coordinates.

    Args:
        mg (RasterModelGrid): The RasterModelGrid object.
        coords (tuple): The (x, y) coordinates of the outlet.

    Returns:
        np.ndarray: A boolean mask array where True indicates the basin area.
    """
    # Initialize DepressionFinderAndRouter and map depressions
    depression_finder = DepressionFinderAndRouter(mg)
    depression_finder.map_depressions()

    # Run FlowAccumulator to calculate flow directions
    flow_accumulator = FlowAccumulator(mg)
    flow_accumulator.run_one_step()

    # Convert coordinates to grid indices and then to a node
    x, y = coords
    row = int((y - mg.xy_of_lower_left[1]) / mg.dy)
    col = int((x - mg.xy_of_lower_left[0]) / mg.dx)
    outlet_node = mg.grid_coords_to_node_id(row, col)

    # Delineate basin from the outlet node
    receivers = mg.at_node["flow__receiver_node"]
    basin_mask = np.zeros(mg.number_of_nodes, dtype=bool)

    # Use a stack to traverse upstream nodes
    stack = [outlet_node]
    while stack:
        node = stack.pop()
        if not basin_mask[node]:
            basin_mask[node] = True
            # Add all nodes that flow into the current node
            stack.extend(np.where(receivers == node)[0])

    return basin_mask


def main():
    # Open the raster file and get the data and metadata
    filename = "./assets/rst/clippedDem_12N.tif"
    rasterObj = getRasterObject(filename)

    # Create a RasterModelGrid from the raster object
    mg = CreateGridFromDEM(rasterObj, add_elev=True)

    # Define the basin mask from the outlet coordinates
    basin_mask = define_basin_from_coords(mg, (rasterObj.bounds[0], rasterObj.bounds[1]))

    # Show the basin mask
    plt.imshow(basin_mask.reshape(mg.shape), cmap="gray", origin="lower")
    plt.title("Watershed Basin")
    plt.colorbar(label="Basin Mask")
    plt.show()


if __name__ == "__main__":
    main()
