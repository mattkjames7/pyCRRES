import numpy as np
from .. import Globals

def _GetFileName(line,ext):
	
	s = line.split('"')
	if s[1].endswith(ext):
		url = s[1]
	else:
		url = None
		
	i0 = line.find('<tt>')
	i1 = line.rfind('</tt>')
	
	if i0 > -1 and i1 > -1:
		fname = line[i0+4:i1]
	else:
		fname = None
	if not fname.endswith(ext):
		fname = None
		
	return url,fname
		
def _DownloadHTTP(url,ext):
	'''
	Download the HTTP file and return a list of file names and URLs
	
	'''
	
	#set up a temporary file/path 
	tmppath = Globals.DataPath+'tmp/'
	if not os.path.isdir(tmppath):
		os.system('mkdir -pv '+tmppath)
	tmpfname = tmppath + '{:17.7f}.tmp'.format(time.time())
	
	#wget the file
	ret = os.system('wget --no-verbose '+url+' -O '+tmpfname)

	#read it in
	lines = pf.ReadASCIIFile(tmpfname)
	
	#scan for files
	if ext[0] != '.':
		ext = '.' + ext
	files = []
	urls = []
	for i in range(0,lines.size):
		if ext in lines[i] and 'href' in lines[i]:
			u,f = _GetFileName(lines[i],ext)
			if not u is None and not f is None:
				files.append(f)
				urls.append(u)
				
	return urls,fnames
