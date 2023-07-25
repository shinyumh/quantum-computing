#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""


def main() -> None:

    # since we want -44 C to 106 C inclusive, set end = 107
    # because range function's end parameter is exclusive
    for celsius in range(-44, 107, 4):

        # the formula to convert celsius to fahrenheit
        fahrenheit: float = (celsius * 9 / 5) + 32

        # print out C/F pairs
        print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")


if __name__ == "__main__":
    main()
