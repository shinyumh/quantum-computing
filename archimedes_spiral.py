#!/usr/bin/env python3
"""archimedes_spiral.py"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.integrate import quad
from math import sqrt


def f(x):
    """function given"""
    return sqrt(x ** 2 + 1)

def arclength(r1, r2):
    """calculates the arc length of a polar equation r = theta"""

    res, err = quad(f,r1,r2)
    return res

def graphspiral(r1, r2):
    """graphs the spiral of the polar equation"""

    x = []
    y = []

    # convert from polar to cartesian coords
    for t in linspace(r1,r2):
        x.append(t*np.cos(t))
        y.append(t*np.sin(t))

    plt.plot(x,y)  
    plt.show()
    return

def main() -> None:
    # print out the arc length
    print("the arc length is " + str(arclength(0,8 * np.pi)))

    # graph the spiral
    graphspiral(0,8*np.pi)

if __name__ == "__main__":
    main()


#additional comments
'''need to add labels to graph'''
'''score 3'''