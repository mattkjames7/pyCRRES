import numpy as np
import os

#path for the data to be stored
DataPath = os.getenv("CRRES_DATA")
if DataPath is None:
	DataPath = os.getenv("HOME") + "/CRRES"
	print("$CRRES_DATA environment variable not set, using {:s}".format(DataPath))
DataPath = DataPath + "/"

#this is the base URL for the data
repoURL = "http://vmo.igpp.ucla.edu/data1/CRRES/"
