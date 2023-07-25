#!/usr/bin/env python3
"""sum_squares.py"""

# calculates the sum of 1 to n squared (inclusive)
def sum_square(n: int) -> float:
    
    sum: float = 0.0

    # set end = n + 1 to make sure n is included
    for i in range(1, n + 1):
        sum += i * i

    return sum


def main() -> None:
    # calls the sum_square function to calculate sum of first 1000 naturals squared
    loop_sum: float = sum_square(1000)

    # equation of Gauss sum: sum(n^2) = n(n+1)(2n+1) / 6
    gauss_sum: float = 1000 * (1000 + 1) * (2 * 1000 + 1) / 6

    # prints out answer with comma as the thousand's separator
    print(f"Loop sum = {loop_sum:,}")
    print(f"Gauss sum = {gauss_sum:,}")


if __name__ == "__main__":
    main()



#additional comments:

'''turn description of functions into doc strings'''