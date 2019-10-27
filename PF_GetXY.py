
import os
import numpy as np

def GetXY_ParFlow_1D_100(pf_file,path="",ignore=1):

    # read CrunchFlow data
    filename = os.path.join(path,pf_file)
    f = open(filename,'r')
    lines = f.readlines()
    f.close()

    # ignore lines
    for i in range(ignore):
      lines.pop(0)

    # extract data x0, x1, ..., xN-1 per line, keep only two columns
    xv=[]
    yv=[] 
    for line in lines:
      yv = yv + [float(line.split()[0])]
    
    # hardcoded for 100 cells with 100 length
    xv = np.linspace(0.5,99.5,100)
    yv = np.array(yv)

    return (xv, yv)
