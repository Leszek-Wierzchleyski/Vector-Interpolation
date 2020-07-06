import numpy as np
import matplotlib.pyplot as plt


def VectorInt2D(fgrid, xp, yp):

    """Interpolates between values on a  2D grid, where the values of the function are known at the vertices on the 
    grid. Approximates the function at a position (xp,yp) where the value of the function is unknown. 
    fgrid must be a 2D numpy array"""

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


def VectorInt3D(fgrid, xp, yp, zp):

    """Interpolates between values on a 3D lattice, where the values of the function are known at the vertices on the
    lattice. Approximates the function at a position (xp,yp,zp) where the function is unknown. fgrid must be a 3D
    numpy array"""

    x1 = int(np.floor(xp))

    x2 = int(np.ceil(xp))

    y1 = int(np.floor(yp))

    y2 = int(np.ceil(yp))

    z1 = int(np.floor(zp))

    z2 = int(np.ceil(zp))

    if xp - x1 == 0:
        x1 = xp - 1
        x2 = xp + 1
    if yp - y1 == 0:
        y1 = yp - 1
        y2 = yp + 1
    if zp - z1 == 0:
        z1 = zp - 1
        y2 = zp + 1

    xd = (xp - x1) / (x2 - x1)

    yd = (yp - y1) / (y2 - y1)

    zd = (zp - z1) / (z2 - z1)

    c00 = fgrid[y1,x1,z1] * (1 - xd) + fgrid[y1,x2,z1] * xd

    c01 =  fgrid[y1,x1,z2] * (1 - xd) + fgrid[y1,x2,z2] * xd

    c10 = fgrid[y2,x1,z1] * (1 - xd) + fgrid[y2,x2,z1] * xd

    c11 = fgrid[y2,x1,z2] * (1 - xd) + fgrid[y2,x2,z2] * xd

    c0 = c00 * (1 - yd) + c10 * yd

    c1 = c01 * (1 - yd) + c11 * yd

    c = c0 *(1 - zd) + c1 * zd

    return c
