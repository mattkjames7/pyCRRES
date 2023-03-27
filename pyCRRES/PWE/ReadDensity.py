from . import Globals
import numpy as np
import os
import RecarrayTools as RT

def ReadDensity():
    '''
    read the whole dataset in!
    
    '''
    fname = Globals.InstPath + 'density.bin'
    return RT.ReadRecarray(fname)