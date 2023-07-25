#!/usr/bin/env python3
"""plot_ellipse.py"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, cos, sin


def main() -> None:

    radianlist = []
    radii = [0.0] * 1000

    # first, find about 1000 points between 0 and 2pi
    for i in range(1000):
        radianlist.append(2 * np.pi / 1000 * i)

    # then, for every angle, calculate the radius from the center of the ellipse
    for i in range(len(radianlist)):
        # to convert from cartesian to polar, x = rcos(theta) and y = rsin(theta)
        # so the equation turns into r^2cos^2 / 100^2 + r^2sin^2 / 50^2 = 1
        # which is equation to r^2cos^2 + 4r^2sin^2 = 100^2
        # so r = sqrt(100^2 / (cos^2 + 4sin^2))

        current = radianlist[i]
        radii[i] = 100 * sqrt(1 / (cos(current) ** 2 + 4 * sin(current) ** 2))
        # print(current,cos(current), sin(current))

    xvalues = []
    yvalues = []

    # combine the radii and radianlist together
    combo = list(zip(radii,radianlist))

    for radius, radian in combo:
        # x = rcos(theta)
        xvalues.append(radius * cos(radian))

        # y = rsin(theta)
        yvalues.append(radius * sin(radian))

    # plot & add labels
    plt.plot(xvalues, yvalues)
    plt.title(f"$x^2/100^2 + y^2/50^2 = 1$")
    plt.xlabel(f"x")
    plt.ylabel(f"y")
    plt.show()

if __name__ == "__main__":
    main()
