#!/usr/bin/env python3
"""random_walk_gamma.py"""

from scipy.special import gamma
from math import sqrt
import matplotlib.pyplot as plt

def randomwalk(n):
    """calculate and plots the expected final distance of a random walk of n steps on a unit lattice having dimension d"""
    dimen = []

    # evenly find 100 values from between 1 - 25
    for i in range(101):
        dimen.append((24 / 100 * i) + 1)


    expected = []

    # calculate the expected value of the final distance for every dimension
    # using the scipy function, scipy.special.gamma, and the equation given
    for d in dimen:
        expected.append(sqrt(2 * n / d)*((gamma((d + 1) / 2)) / gamma(d/2)) ** 2)

    plt.plot(dimen,expected)
    plt.xlabel("dimensions")
    plt.ylabel("expected final distance")
    plt.show()

    # print out the result
    # for d, e in list(zip(dimen, expected)):
    #     print(f"for distance {d}, the expected value is {e}")

def main() -> None:
    randomwalk(20000)

if __name__ == "__main__":
    main()
