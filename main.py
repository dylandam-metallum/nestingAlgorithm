import ezdxf as ez
import dxfClass as dc
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib import axes
import numpy as np
import math
import functions as func

try:
    doc = ez.readfile('Drawing18_DylanTest.dxf')
except:
    print('No File')

msp = doc.modelspace()

# Creating the sheet
ms = dc.sheet(8000, 8000)

num = 0
coord = []
for e in msp:
    if e.dxftype() == 'LINE':
        num+=1
        startpoints = [e.dxf.start[0], e.dxf.start[1]]
        endpoints = [e.dxf.end[0], e.dxf.end[1]]
        line = dc.contour(startpoints, endpoints , 'LINE')
        coord.append(line)
    elif e.dxftype() == 'ARC':
        num+=1
        startpoints = [e.start_point[0], e.start_point[1]]
        endpoints = [e.end_point[0], e.end_point[1]]
        line = dc.contour(startpoints, endpoints , 'ARC')
        coord.append(line)
    elif e.dxftype() =='CIRCLE':
        num+=1
    else:
        pass

listarr = []
for i in range(len(coord)):
    coord[i].start = func.twoDrotation(coord[i].start, 180)
    coord[i].end = func.twoDrotation(coord[i].end, 180)
    listarr.append(coord[i].start)
    listarr.append(coord[i].end)
    print(i)
    print(coord[i].lineType)
    print(coord[i].start)

xpoint = []
ypoint = []

for i in range(len(listarr)):
    xpoint.append(listarr[i][0])
    ypoint.append(listarr[i][1])


ms.sheetPlot.plot(xpoint,ypoint)
ms.sheetPlot.show()


