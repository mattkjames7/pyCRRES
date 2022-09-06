import numpy as np
import os

def _DownloadFiles(url,fnames,path,Overwrite):
	
	#loop through each file
	nf = len(fnames)
	for i in range(0,nf):
		print('\rDownloading file {:d} of {:d}'.format(i+1,nf),end='')
		furl = url + fnames[i]
		fout = path + fnames[i]
		if Overwrite or not os.path.isfile(fout):
			os.system('wget --no-verbose '+furl+' -O '+fout)
	print()
	
	
