#!/usr/bin/env python3
"""euler_curve.py"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from sympy import *


def x(u):
    return np.cos(u**2)


def y(u):
    return np.sin(u**2)


def main() -> None:
    t = np.linspace(0, 12.34, 1000)
    a = [quad(x, 0, i) for i in t]
    b = [quad(y, 0, i) for i in t]

    plt.plot(a, b, "r")

    w = symbols("x")
    xcoord = N(integrate(cos(w**2), (w, 0, np.inf)))
    # print(xcoord)

    z = symbols("x")
    ycoord = N(integrate(sin(z**2), (z, 0, np.inf)))
    # print(ycoord)

    plt.scatter([xcoord], [ycoord])

    plt.title("arc length: " + str(12.34))
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


if __name__ == "__main__":
    main()
