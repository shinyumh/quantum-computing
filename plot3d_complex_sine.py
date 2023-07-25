#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def f(x):
    return abs(np.sin(x))

def plot(ax: Axes) -> None:
    real: NDArray[np.float_] = np.linspace(-2.5, 2.5, 100)
    imag: NDArray[np.float_] = np.linspace(-1, 1, 100)

    data = real + 1j * imag

    x,y = np.meshgrid(real,imag)

    z = f(data)

    ax.plot_surface(x,z,y,cmap=cm.coolwarm)

    ax.set_xlabel("real")
    ax.set_ylabel("f(z)")
    ax.set_zlabel("imag")  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
