import arcpy

# Set geoprocessing environments

arcpy.env.workspace = r"C:\Users\Jon\ArcGIS Data\GEOG 650\Week 4\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True

# Create list of feature classes in SanJuan.gdb

fcList = arcpy.ListFeatureClasses()

# Create a loop to buffer Lakes and Streams

bufferList = [] 

for fc in fcList:
    if fc == "Lakes" or fc == "Streams":
        arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters", "", "", "all")
        bufferList.append(fc + "Buffer")

arcpy.Union_analysis(bufferList, "WaterBuffers")