#!/usr/bin/env python3
"""benfords_law.py"""

import random
import matplotlib.pyplot as plt


def benfords(num: int):

    # create a list to keep track of the sig digits of each randomly generated num
    signum = []

    for _ in range(0, num):
        # generate a random number between 1 and 1000000 inclu.
        init: int = random.randint(1, 1000000)
        pwr = str(init ** 100) # raise to 10th power
        signum.append(pwr[0]) # add first digit to list

    signum.sort()

    # plot using plt.hist
    plt.hist(signum)

    plt.show()
    return
    


def main() -> None:
    random.seed(2023)

    # want 10000 rand nums
    benfords(100000)


if __name__ == "__main__":
    main()

#additional comments
'''odd split in graph, try using bar instead of hist to plot graph'''
''score 3'''