#!/usr/bin/env python3
"""eulers_constant.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

from numpy import log
from scipy.integrate import quad


def f(x):
    """function given"""
    return log(log(1 / x))

def eulersconst():
    """calculates the eulers constant using scipy"""

    res, err = quad(f,0,1)

    return 0 - res

def harmonicnums(num):
    """calculate harmonic nums"""

    list = []
    acc = 0
    
    for i in range(1,num + 1):
        acc += 1 / i
        list.append(acc)

    return list

def plot(ax: Axes) -> None:
    
    # graph harmonic numbers on a step graph
    harmonic = harmonicnums(50)

    # fmt: off
    ax.step(range(50), harmonic, color="black", linewidth=2,
            label="harmonic numbers")
    # fmt: on


    # graph equation given
    x: NDArray[np.float_] = np.linspace(0, 50, 200, dtype=np.float_)
    y: NDArray[np.float_] = eulersconst() + log(x)

    # fmt: off
    ax.plot(x, y, color="blue",
            label=r"line graph of gamma + ln(x)")
    # fmt: on

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 5)
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.grid()
    ax.set_title(f"task 10-03")
    ax.set_xlabel("x values")
    ax.set_ylabel("y values")
    ax.legend()


def main() -> None:
    # print out eulers const
    print(eulersconst())

    # graph the plot
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

    # print(harmonicnums(5))

if __name__ == "__main__":
    main()


'''score 4'''