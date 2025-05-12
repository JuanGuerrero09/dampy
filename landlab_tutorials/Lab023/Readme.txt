Introduction

This lab is targeted at undergraduate students and illustrates how storm sequences interact with watershed properties to control infiltration and runoff.
Students will first use the PrecipitationDistribution landlab component to generate two month-long rainfall time series over the Hugo watershed: a higher intensity and a lower intensity scenario. Students will learn about rainfall intensity and storm parameters, and will use pandas to read a .csv and matplotlib to plot the rainfall time series.

Next, students will model what happens to the rain when it reaches the ground. Students will use the landlab component SoilInfiltrationGreenAmpt to model rainfall infiltration and will explore how hydraulic conductivity and hydraulic gradient affect the infiltration rate. The propagation of surface runoff will be simulated using the OverlandFlow component. Students will plot the resulting hydrographs and infiltration depths using matplotlib, and can explore how adjusting different parameters affects these outputs.

The lab includes assignment questions that prompt students to think about and explore how adjusting parameters for each aspect of the system - storm sequences and watershed properties - affects runoff and infiltration.

Classroom organization
Students can work through the lab exercise alone or in small groups.

Learning objectives
Skills
Communicate between two LandLab components with inputs and outputs
Set up a topographic elevation grid from an ascii file
Create plots using `matplotlib`
Read inputs from .csv file
Use pandas DataFrames
Key concepts
Concepts of rainfall intensity, storm depth, and hydraulic conductivity
Relationships between infiltration depth and hydraulic conductivity
Relationships between rainfall intensity distribution and hydrographs

Lab notes
For each section, read through the conceptual section first, then try running the python cells. Try adjusting different parameters on your own and see what happens to the outputs. Then answer the assignment questions at the end. Answering the questions will require you to adjust aspects of the code.

This lab can be run on the lab (for educators) and jupyter (for general use) instances of the OpenEarthscape JupyterHub: just click one of the links under the Run online using heading at the top of this page, then run the notebook in the "CSDMS" kernel.

If you don't already have a JupyterHub account, follow the instructions to sign up at https://csdms.colorado.edu/wiki/JupyterHub. If you're an educator, you can get JupyterHub accounts for students--please contact us through the CSDMS Help Desk: https://csdms.github.io/help-desk.


Requirements
If run locally, this lab requires the installation of the following Python packages: landlab, numpy, random, matplotlib, and pandas

Acknowledgements
This lab builds on the “Coupled rainfall-runoff model with OverlandFlow” landlab tutorial and was created as part of the NSF-funded 2020 CSDMS ESPIn (Earth Surface Processes Institute) program.

References
B Campforts, I Overeem, NM Gasparini, M Piper, L Arthurs, 2021: Modeling earth surface processes for the future: ESPIn, a summer school focusing on cyber training and professional networking, 2021 AGU Fall Meeting, New Orleans, LA.