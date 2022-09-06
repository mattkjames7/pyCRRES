import numpy as np
from . import Globals
from .. import Common
import os

def Download(Overwrite=False):
	'''
	This will attempt to download all of the densities.
	
	'''
	
	#get the path to download data to
	path = Globals.InstPath + 'density/'
	Common.CheckDir(path)
	
	#file extension
	ext = '.DEN'
	
	#url to download from
	url = Globals.uclaURL + 'PWE/PT8S/'
	
	#call the download function
	Common.Download(url,ext,path,Overwrite=Overwrite)
	
	
