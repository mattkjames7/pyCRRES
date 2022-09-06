import numpy as np
from .CheckDir import CheckDir
from ._ListFiles import _ListFiles
from ._DownloadFiles import _DownloadFiles

def Download(url,ext,path,Overwrite=False):
	
	
	#make sure the output directory exists
	CheckDir(path)
	
	#call the function to list the urls and filenames
	urls,fnames = _ListFiles(url,ext)

	#downlaod them
	_DownloadFiles(url,fnames,path,Overwrite)


