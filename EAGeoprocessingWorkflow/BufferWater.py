import arcpy # this staement allows the environment to access the tools for a GIS type project.

# Set geoprocessing environments

arcpy.env.workspace = r"C:\Users\Jon\ArcGIS Data\GEOG 650\Week 4\PythonGP\Data\SanJuan.gdb" # This line establishes the wokspace, to where the information created will be returned.
arcpy.env.overwriteOutput = True # This line makes it possible to run this code and replace the existing Feature class that is created. 

# Create list of feature classes in SanJuan.gdb

fcList = arcpy.ListFeatureClasses() # This creates an open feature class list that will be populated below.

# Create a loop to buffer Lakes and Streams

bufferList = [] # This line creates and open list feature that will be appended to as the correct feature classes are located in the data.

for fc in fcList: # A for loop has been created to process though the data to find the information needed to complete the buffer.
    if fc == "Lakes" or fc == "Streams": # This line is searching for lakes and streams if it finds one then then it processed to the next line.
        arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters", "", "", "all") # In this line the lakes or streams are buffered and set as a temp value for the next line
        bufferList.append(fc + "Buffer") # This line take the above output and appends it to the empty list created in line 14.

arcpy.Union_analysis(bufferList, "WaterBuffers") # This union process will combine all the "bufferList" and put it out as a new feature class called "WaterBuffer."