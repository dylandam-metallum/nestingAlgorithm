import matplotlib.pyplot as plot
import matplotlib.pyplot as plt


class contour():
    # Class for the shapes
    lineType = ''
    start = []
    end = []

    def __init__(self,listA,listB,name):
        self.start = listA
        self.end = listB
        self.lineType = name

class sheet():
    # Sheet size
    x = 0
    y = 0
    sheetPlot = plt

    def __init__(self, a, b):
        self.x = a
        self.y = b
        self.sheetPlot.axis([0, self.x, 0, self.y])

    def showPlot(self):
        self.sheetPlot.show()