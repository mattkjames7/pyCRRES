import numpy as np
import os

def CheckDir(path):
	'''
	Checks if a directory exists, then makes it.
	
	'''
	if not os.path.isdir(path):
		os.system('mkdir -pv ' +path)
