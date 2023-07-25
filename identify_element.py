#!/usr/bin/env python3
"""identify_element.py"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from sklearn.linear_model import LinearRegression


def main() -> None:
    t = np.array([-50, 0, 50, 100, 150]).reshape((-1, 1))
    v = np.array([11.6, 14.0, 16.2, 19.4, 21.8])

    t = t + 273.15
    v = v / 1000

    model = LinearRegression().fit(t, v)
    intercept = model.intercept_
    slope = model.coef_

    x = np.linspace(0, 500, 200)
    y = slope * x + intercept

    plt.plot(x, y, "r")

    plt.scatter(t, v)

    # PV = nRT, slope = v / t
    # n = PV / RT = (P/R) * slope

    n = (2 / (8.205 * 10 ** (-5))) * slope
    molar = 50 / n

    plt.title("molar mass: " + str(molar[0]) + " = Argon (Ar)")
    plt.xlabel("temp (K)")
    plt.ylabel("volume (m^3)")

    plt.show()


if __name__ == "__main__":
    main()
