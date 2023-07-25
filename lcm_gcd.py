#!/usr/bin/env python3
"""lcm_gcd.py"""

from math import gcd

# calculates the lcm of 2 integers without looping
def lcm(a: int, b: int) -> int:
    # just in case the user doesn't enter a & b in the right order (a > b)
    if a < b:
        a, b = b, a

    # equation to calculate lcm from gcd
    return a * b // gcd(a,b)


def main() -> None:
    a: int = 447618
    b: int = 2011835

    print(f"The LCM of {a} and {b} = {lcm(a,b)}")


if __name__ == "__main__":
    main()


#additional comments: 

  

'''turn description of functions into doc strings''' 