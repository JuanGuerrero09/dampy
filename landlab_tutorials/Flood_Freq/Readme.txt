Contributor(s)
    Alejandra Ortiz at Colby College.

Introduction

This exercise will provide some experience with methods used for predicting flood frequency and magnitude. We will be using the US Geological Survey (USGS) website to retrieve historical stream gauge data of the sort used to predict the likelihood of flood events of particular magnitudes during a given time interval. Such predictions are the basis for numerous engineering, restoration and development projects in and around rivers. 1. Practice using Python Pandas DataFrames to import, manipulate, and visualize data, 2. Learn some powerful tools for subsetting your dataframes, and 3. Practice visualizing data

Classroom organization
This is for an undergraduate geomorphology course (200 level).

Learning objectives
Skills
Pandas Dataframes
Data Visualization
Subsetting dataframes
Key concepts
Flood Frequency Analyses
Rating Curves
Time-series gaps

Lab notes
Here is a helpful link - https://www.usgs.gov/centers/sa-water/science/flood-frequency-information?qt-science_center_objects=0#qt-science_center_objects
You could include requirements that students check their results for the given rivers (Fishing Creek, Tar River, Ellerbe Creek, and Roanoke River) to the USGS calculations for an extended assignment.

I have adapted a lab similar to this one by SERC (https://serc.carleton.edu/hydromodules/steps/168500.html) from T. Perron using excel to analyze flood frequency of a river into python. It would be easy enough to include more background on Wollman & Miller, geomorphic work, the characterstic flood, extreme value analyses, etc dependent on your course interest and focus.

Please visit https://github.com/ale37911/CSDMS_Labs/tree/main/Flood_Freq for associated files (data and instructor Notebook).

This lab can be run on the lab (for educators) and jupyter (for general use) instances of the OpenEarthscape JupyterHub: just click one of the links under the Run online using heading at the top of this page, then run the notebook in the "CSDMS" kernel.

If you don't already have a JupyterHub account, follow the instructions to sign up at https://csdms.colorado.edu/wiki/JupyterHub. If you're an educator, you can get JupyterHub accounts for students--please contact us through the CSDMS Help Desk: https://csdms.github.io/help-desk.


Requirements
If run locally, this lab requires the installation of the Python packages numpy, pandas, and matplotlib, as well as peak annual stream and daily discharge data for a given location.

Acknowledgements
CSDMS and Mark Piper provided support for the creation and hosting of my jupyter hub notebooks