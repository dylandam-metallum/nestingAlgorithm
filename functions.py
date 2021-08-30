import numpy as np


def break_arcs(arc):
    # This function breaks arcs into 2 lines. from start -> mid then mid -> end

    return

def twoDrotation(xy,theta):
    rad = np.radians(theta)
    rotmatrix =  np.array(((np.cos(rad), -np.sin(rad)),(np.sin(rad),np.cos(rad))))
    return rotmatrix.dot(xy)