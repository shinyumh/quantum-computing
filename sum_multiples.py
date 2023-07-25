#!/usr/bin/env python3
"""sum_multiples.py"""

def sum_div(n : int) -> int:
    sum: int = 0

    # since we want all naturals less than 1900, set the range from 1 to 1900 exclusive
    for number in range(1,n):

        # x is divisible by a number means x mod that number is 0
        # or in other words, when x is divided by that number, there is no remainder
        if number % 7 == 0 and number % 11 == 0:

            # only add it to sum when it satisfies both conditions
            sum += number

    return sum

def main() -> None:
    ans: int = sum_div(1900)

    print(f"Sum = {ans:,}")

if __name__ == "__main__":
    main()




#additional comments: 

  

'''turn description of functions into doc strings''' 