#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

from __future__ import annotations

import typing

from math import sqrt, exp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def pdf_mb(x,a):
    """"returns the pdf of maxwell_boltzmann distribution"""
    return sqrt(2 / np.pi) * ((x ** 2) / (a ** 3)) * exp((0-(x**2)) / (2 * (a ** 2)))

def plot(ax: Axes) -> None:

    # List of integers from 0 to 20 (inclusive)
    r_values: list[int] = list(range(21))

    # calculate the pdf of mb where a = 1, a = 2, and a = 5
    dist1: NDArray[np.float_] = np.asarray(
        [pdf_mb(i, 1) for i in r_values], dtype=np.float_
    )
    dist2: NDArray[np.float_] = np.asarray(
        [pdf_mb(i, 2) for i in r_values], dtype=np.float_
    )
    dist3: NDArray[np.float_] = np.asarray(
        [pdf_mb(i, 5) for i in r_values], dtype=np.float_
    )

    # graph onto same plot
    plt.plot(r_values, dist1, label="a = 1")
    plt.plot(r_values, dist2, label="a = 2")
    plt.plot(r_values, dist3, label="a = 5")

    ax.set_title(f"pdf of maxwell boltzmann distribution")
    ax.set_xlabel("x range")
    ax.set_ylabel("probability")

    ax.legend(loc="upper right")

    ax.xaxis.set_major_locator(MultipleLocator(5))


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()



'''score 4'''