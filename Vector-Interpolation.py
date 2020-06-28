import numpy as np
import matplotlib.pyplot as plt


def VectorInt2d(f, fx, fy, fxy, x0, xf, y0, yf, N):

    """Implements a bicubic interpolation method for a two dimensional grid of size NxN unit squares with xf,yf and
    x0,y0 being the largest and smallest values respectively. The function f must be smooth and the partial derivatives
    fx, fy and fxy must be known """

    x = np.linspace(x0,xf,N,dtype=int)


    y = np.linspace(y0,yf,N,dtype=int)

    a = np.array([[x],[y]])

    plist = []

    for i in x-1:
        for j in y-1:
            FirstArray = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [-3, 3, -2, -1], [2, -2, 1, 1]])

            FunctionArray = np.array([[f(x[i], y[j]), f(x[i], y[j+1]), fy(x[i], y[j]), fy(x[i], y[j+1])],
            [f(x[i+1], y[j]), f(x[i+1], y[j+1]), fy(x[i+1], y[j]), fy(x[i+1], y[j+1])],
            [fx(x[i], y[j]), fx(x[i], y[j+1]), fxy(x[i], y[j]), fxy(x[i], y[j+1])],
            [fx(x[i+1], y[j]), fx(x[i+1], y[j+1]), fxy(x[i+1], y[j]), fxy(x[i+1], y[j+1])]])

            SecondArray = np.array([[1, 0, -3, 2], [0, 0, 3, -2], [0, 1, -2, 1], [0, 0, -1, 1]])

            IntermediateArray = np.matmul(FirstArray, FunctionArray)

            Alpha = np.matmul(IntermediateArray, SecondArray)

            px = np.array([[1, x[i], x[i]**2, x[i]**3]])

            py = np.array([[1], [y[j]], [y[j]**2], [y[j]**3]])

            pint = np.matmul(px, Alpha)

            p = np.matmul(pint, py)

            plist.append(p)

    return plist
