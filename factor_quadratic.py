#!/usr/bin/env python3
"""factor_quadratic.py"""

from math import gcd

def factor_quadratic(h: int, i: int, j: int) -> None:
    """Displays factors of the quadratic polynomial Jx^2 + Kx + L"""

    print(f"Given the quadratic:{h}x^2 + {i}x + {j}")

    # added to first factor out the gcd shared between all coeffs
    factor = gcd(gcd(h,i),j)
    print(f"the gcd among the three numbers is {factor}")
    h,i,j = h // factor, i // factor, j // factor

    # ans = False

    # for multiple in range(1, 10000):
    #     h, i, j = h * multiple, i * multiple, j * multiple
    for a in range(1, h + 1):
        if h % a == 0:
            c: float = h / a
            for b in range(1, j + 1):
                if j % b == 0:
                    d: float = j / b
                    if a * d + b * c == i:
                            # a2 = a / multiple
                            # b2 = b / multiple
                            # c2 = c / multiple
                            # d2 = d / multiple
                            # print(f"The factors are: ({a2}x + {b2})({c2}x + {d2})")
                        print(f"The factors are: ({a}x + {b})({c}x + {d})")
                        return

    # if reach this point, it cannot be factored
    # source: professor's answer
    print(f"cannot be factored since the polynomial includes prime coefficients")

def main() -> None:
    factor_quadratic(115425, 3254121, 379021)


if __name__ == "__main__":
    main()
