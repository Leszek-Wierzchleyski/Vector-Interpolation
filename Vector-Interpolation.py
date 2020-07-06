import numpy as np
import matplotlib.pyplot as plt


def VectorInt2D(fgrid, xp, yp):

    """Interpolates between values on a  2D grid, where the values of the function are known at the vertices on the 
    grid. Approximates the function at a position (xp,yp) where the value of the function is unknown. 
    fgrid must be a numpy array"""

    x1 = int(np.floor(xp))

    x2 = int(np.ceil(xp))

    y1 = int(np.floor(yp))

    y2 = int(np.ceil(yp))
   
    if xp - x1 == 0:
        x1 = xp - 1
        x2 = xp + 1
    if yp - y1 == 0:
        y1 = yp - 1
        y2 = yp + 1

    fxp1 = ((x2 - xp) / (x2 - x1)) * fgrid[y1,x1] + ((xp - x1) / (x2 - x1)) * fgrid[y1,x2]

    fxp2 = ((x2 - xp) / (x2 - x1)) * fgrid[y2,x1] + ((xp - x1) / (x2 - x1)) * fgrid[y2,x2]

    fxpyp = ((y2 - yp) / (y2 - y1)) * fxp1 + ((yp - y1) / (y2 - y1)) * fxp2

    return fxpyp
