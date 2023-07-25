#!/usr/bin/env python3
"""plot3d_cylinder.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 100)  # poloidal angle

    x: NDArray[np.float_] = np.cos(theta)
    y: NDArray[np.float_] = np.sin(theta)
    a, z = np.meshgrid(theta,np.linspace(0,1,100))

    ax.plot_wireframe(x, y, z)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
