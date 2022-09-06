import numpy as np
import os

#path for the data to be stored
DataPath = os.getenv("CRRES_DATA")
if DataPath is None:
	DataPath = os.getenv("HOME") + "/CRRES"
	print("$CRRES_DATA environment variable not set, using {:s}".format(DataPath))
DataPath = DataPath + "/"

#these are the base URLs for the data
# Ephemeris, LPI, MAG, PWE
uclaURL = "http://vmo.igpp.ucla.edu/data1/CRRES/"
# attitude, ephemeris, magnetic field, heef, mea, onr604, protel
spdfURL = "https://spdf.gsfc.nasa.gov/pub/data/crres/"
