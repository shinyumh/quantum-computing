#!/usr/bin/env python3
"""ladder_problem.py"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize


# citation: based on professor's solutions

# define the function
def f(x):
    return 2 / np.sin(x) + 1 / np.cos(x)

def plot(ax):

    # create the x values and the y values
    x = np.linspace(0, np.pi / 2, 100)[1:-2]
    ladder = f(x)

    # plot it
    ax.plot(x,ladder)

    # find the optimal theta
    res = scipy.optimize.minimize(f, np.pi/4)

    # len is the max length given the theta
    theta = res.x[0]
    len = float(f(np.array(theta)))

    ax.set_title(f"max length = {len:.4f}")

    ax.plot(theta,len, marker = "o")

    ax.set_xlabel("radian")
    ax.set_ylabel("length")

    ax.set_ylim(0,25)

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()