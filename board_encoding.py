#!/usr/bin/env python3
"""board_encoding.py"""


def decode_board(n:int) -> None:
    
    # steps to decoding:
    # 1. convert encoding to base 3
    # 2. reverse the base 3 representation & add zeros to end
    # 3. first 3 of rep = row 1, second 3 of rep = row 2, etc.

    # convert number to base 3
    base3 = []
    
    while n != 0:
        base3.append(n % 3)
        n = n // 3

    # fill in zeros at the end until length reaches 9
    while len(base3) < 9:
        base3.append(0)

    # right now, the base3 list is the REVERSED base 3 rep of n
    # so just get row 1, row 2, and row 3 from the representation
    
    row1 = base3[0:3]

    row2 = base3[3:6]

    row3 = base3[6:]

    print(row1)
    print(row2)
    print(row3)

    return

def main() -> None:
    print("board num: 2271")
    decode_board(2271)

    print("board num: 1638")
    decode_board(1638)

    print("board num: 12065")
    decode_board(12065)

if __name__ == "__main__":
    main()


#additional comments
'''good use of the mod function'''
'''score 4'''