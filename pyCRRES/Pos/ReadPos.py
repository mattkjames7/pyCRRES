import numpy as np
import PyFileIO as pf
import os
from .. import Globals
import RecarrayTools as RT
import DateTimeTools as TT

def ReadPos():
    
	fname = Globals.DataPath + 'crres.bin'

	if not os.path.isfile(fname):
		#extract
		os.system('cp -v '+Globals.ModulePath+'__data/crres.dat.tar.gz '+Globals.DataPath)
		os.system('tar -xvf '+Globals.DataPath+'crres.dat.tar.gz -C '+Globals.DataPath)

		dtype0 = [ 	('Year','int32'),
					('doy','int32'),
					('hms','object'),
					('xgsm','float32'),
					('ygsm','float32'),
					('zgsm','float32'),]
		dname = Globals.DataPath + 'crres.dat'
		data0 = pf.ReadASCIIData(dname,Header=False,dtype=dtype0)

		dtype = [	('Date','int32'),
	   				('ut','float32'),
					('utc','float64'),
					('xgsm','float32'),
					('ygsm','float32'),
					('zgsm','float32'),]
		
		data = np.recarray(data0.size,dtype=dtype)

		data.Date = TT.DayNotoDate(data0.Year,data0.doy)
		for i in range(0,data.size):
			h,m,s = np.int32(data0.hms[i].split(':'))
			data.ut[i] = TT.HHMMtoDec(h,m,s)
		data.utc = TT.ContUT(data.Date,data.ut)
		data.xgsm = data0.xgsm
		data.ygsm = data0.ygsm
		data.zgsm = data0.zgsm	

		RT.SaveRecarray(data,fname,StoreDtype=True)
	else:
		data = RT.ReadRecarray(fname)

	return data