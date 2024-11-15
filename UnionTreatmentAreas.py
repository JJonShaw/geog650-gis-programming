import arcpy

# Set geoprocessing environments

arcpy.env.workspace = r"C:\Users\Jon\ArcGIS Data\GEOG 650\Week 4\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True

# Create Python list of treatment area feature classes

treatmentList = ["RoadBuffers", "WaterBuffers"]

# Union treatment areas

arcpy.Union_analysis(treatmentList,"NonChemical")