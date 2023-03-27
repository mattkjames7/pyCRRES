import numpy as np
from ..Common.ListFiles import ListFiles
import PyFileIO as pf
import RecarrayTools as RT
from . import Globals
import DateTimeTools as TT

def _ReadFile(fname):

	dtype0 = [	('VTCW','object'),
	   			('yrdoy','int32'),
				('time','object'),
				('fce','float32'),
				('fuhr','float32'),
				('fpe','float32'),
				('ne','float32'),
				('id','int32'),
				('M','U1')]
	lines = pf.ReadASCIIFile(fname)
	data = pf.ReadASCIIData(lines[2:-1],Header=False,SkipLines=0,dtype=dtype0)

	dtype = [	('Date','int32'),
	   			('ut','float32'),
				('utc','float64'),
				('fce','float32'),
				('fuhr','float32'),
				('fpe','float32'),
				('ne','float32')]	

	n = data.size
	out = np.recarray(n,dtype=dtype)

	yr = data.yrdoy//1000 + 1900
	doy = data.yrdoy % 1000

	out.Date = TT.DayNotoDate(yr,doy)
	hh = []
	mm = []
	ss = []
	for i in range(0,n):
		s = data.time[i].split(':')
		hh.append(np.int32(s[0]))
		mm.append(np.int32(s[1]))
		ss.append(np.int32(s[2]))

	hh = np.array(hh)
	mm = np.array(mm)
	ss = np.array(ss)
	out.ut = TT.HHMMtoDec(hh,mm,ss)
	out.fce = data.fce
	out.fuhr = data.fuhr
	out.fpe = data.fpe
	out.ne = data.ne

	#remove elements where everything is filled with 0s
	good = np.where(yr > 1900)[0]
	out = out[good]

	#sort and then add utc
	srt = np.lexsort((out.ut,out.Date))
	out = out[srt]
	out.utc = TT.ContUT(out.Date,out.ut)

	return out

def Convert():
    
	path = Globals.InstPath + 'density/'
	files = ListFiles(path)
	nf = files.size

	data = []
	n = 0
	for i in range(0,nf):
		print('\rReading file {:d} of {:d}'.format(i+1,nf),end='')
		try:
			data.append(_ReadFile(files[i]))
		except:
			print('\nReading file failed: {:s}\n'.format(files[i]))
			data.append(np.recarray(0,dtype=data[i-1].dtype))
		n += data[i].size
	print()

	out = np.recarray(n,dtype=data[0].dtype)
	p = 0
	for i in range(0,nf):
		print('\rCombining file {:d} of {:d}'.format(i+1,nf),end='')
		out[p:p+data[i].size] = data[i]
		p += data[i].size
	print()

	#sort by time
	srt = np.argsort(out.utc)
	out = out[srt]


	fname = Globals.InstPath + 'density.bin'
	RT.SaveRecarray(out,fname,StoreDtype=True)
	print('Saved '+fname)