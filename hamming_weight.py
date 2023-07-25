#!/usr/bin/env python3
"""hamming_weight.py"""

def hamming_weight1(n:int) -> int:
    """returns the hamming weight of an integer using bin() function"""
    
    # convert to binary first
    binary = bin(n)
    counter = 0

    # count # of ones
    for bit in binary:
        if bit == '1':
            counter += 1
    
    return counter

def hamming_weight2(n:int):
    """returns the hamming weight of an integer WITHOUT using bin() function"""
    counter:int = 0

    # use masking to find # of ones
    # since the & operator only result in 1 when both numbers are ones,
    # n & (n-1) counts one 1 during every iteration & update n accordingly
    while n != 0:
        n = n & (n - 1)
        counter += 1

    return counter

def main() -> None:
    n = 95601
    # print(bin(n))

    print(f"The Hamming Weight of {n} using Python built-in bin() is {hamming_weight1(n)}")
    print(f"The Hamming Weight of {n} without built-in functions is {hamming_weight2(n)}")


if __name__ == "__main__":
    main()