#!/usr/bin/env python3
"""random_walk_gamma.py"""

from scipy.special import gamma

def main() -> None:
    dimen = []

    # evenly find 100 values from between 1 - 25
    for i in range(101):
        dimen.append((24 / 100 * i) + 1)


    expected = []

    # calculate the expected value of the final distance for every dimension
    # using the scipy function, scipy.special.gamma, and the equation given
    for d in dimen:
        expected.append((2 / d)*((gamma((d + 1) / 2)) / gamma(d/2)) ** 2)

    # print out the result
    for d, e in list(zip(dimen, expected)):
        print(f"for distance {d}, the expected value is {e}")

if __name__ == "__main__":
    main()



#additional comments:

'''incorrect output. you need to plot the values'''