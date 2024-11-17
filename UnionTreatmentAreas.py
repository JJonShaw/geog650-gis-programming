import arcpy # This statement allows the environment to access the tools for a GIS type project.

# Set geoprocessing environments

arcpy.env.workspace = r"C:\Users\Jon\ArcGIS Data\GEOG 650\Week 4\PythonGP\Data\SanJuan.gdb" # This line establishes the wokspace, to where the information created will be returned.
arcpy.env.overwriteOutput = True # This line makes it possible to run this code and replace the existing feature class that is created. 

# Create Python list of treatment area feature classes

treatmentList = ["RoadBuffers", "WaterBuffers"] # This line combines our feature classes into one list.

# Union treatment areas

arcpy.Union_analysis(treatmentList,"NonChemical") # this line is used to combind the "treatmentList" and output a feature class called "NonChemical" 