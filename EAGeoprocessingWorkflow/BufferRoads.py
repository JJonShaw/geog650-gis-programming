import arcpy # this staement allows the environment to access the tools for a GIS type project.

# Set the geoprocessing environments

arcpy.env.workspace = r"C:\Users\Jon\ArcGIS Data\GEOG 650\Week 4\PythonGP\Data\SanJuan.gdb" # This line establishes the wokspace, to where the information created will be returned.
arcpy.env.overwriteOutput = True # This line makes it possible to run this code and replace the existing Feature class that is created. 

# Set parameters used to join the BufferDistance table to the Roads feature class

inFeatures = "Roads"
inField = "ROUTE_TYPE"
joinTable = "BufferDistance"
joinField = "ROUTE_TYPE"

# Join table to feature class

arcpy.JoinField_management(inFeatures, inField, joinTable, joinField) # This line will join the information of the selected features to the table. 

# Set parameters used to buffer Roads feature class

outBuffers = "RoadBuffers"
buffField = "DISTANCE"

# Buffer the Roads based on DISTANCE attribute

arcpy.Buffer_analysis(inFeatures, outBuffers, buffField, "", "", "all") # This line is the actual buffer process of the code, I modified it to merge all my output buffers.