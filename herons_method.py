#!/usr/bin/env python3
"""herons_method.py"""

from random import randint

def main() -> None:
    # generate a number randomly
    s = randint(int(1e6),int(2e6))

    # take an initial guess & calculate error
    guess: float = s / 2
    error = s - guess * guess

    # continue to revise guess until error <= 1e-8
    while abs(error) > 1e-8:

        # formula used in herons method
        guess = ((s/guess) + guess) / 2
        error = s - guess * guess

    # print and round guess to 8 digits after decimal point
    print(f"The estimated square root of {s} is {guess:.8f}")

if __name__ == "__main__":
    main()



    #additional comments: 

'''Avoid performing longer calculations in the Main function. It should really be used for declaring inputs for the functions you've already created '''  

  

