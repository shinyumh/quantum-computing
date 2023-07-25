#!/usr/bin/env python3
"""connect_four.py"""


def determine_winner(board:list[list[int]], row:int, col:int, det:int):
    """determine if a board has winner given a non-zero coordinate; board[row][col] == det"""
    # up & down
    count = 1 # since the given coordinate already counts as 1

    # first check downwards by incrementing the row
    pointerrow = row + 1

    # condition of while loop makes sure no index out of bounds
    while pointerrow >= 0 and pointerrow < len(board):
        if board[pointerrow][col] == det:
            count += 1
            pointerrow += 1 # continue checking in the same direction
        else:
            # no need to continue in one direction if one is not det
            # since connect 4 requires the 4 to be connected / consecutive
            break 
    if count >= 4: return True

    # if count is still less than 4, continue checking upwards (no need to reset count since continuity)
    pointerrow = row - 1
    while pointerrow >= 0 and pointerrow < len(board):
        if board[pointerrow][col] == det:
            count += 1
            pointerrow -= 1 
        else:
            break
    if count >= 4: return True

    # left & right
    
    # reset count since left & right is NOT in the same direction as up & down
    count = 1

    # instead of incrementing row, change col this time
    pointercol = col + 1
    while pointercol >= 0 and pointercol < len(board[0]):
        if board[row][pointercol] == det:
            count += 1
            pointercol += 1
        else:
            break
    if count >= 4: return True # again, no need to reset

    # check the left direction
    pointercol = col - 1
    while pointercol >= 0 and pointercol < len(board[0]):
        if board[row][pointercol] == det:
            count += 1
            pointercol -= 1
        else:
            break
    if count >= 4: return True

    # diagonal

    count = 1

    # diagonal means both row and col has to increment by the same amount (1)
    # there are two directions for diagonal
    pointerrow = row + 1
    pointercol = col + 1
    while pointercol >= 0 and pointercol < len(board[0]) and pointerrow >= 0 and pointerrow < len(board):
        if board[pointerrow][pointercol] == det:
            count += 1
            pointerrow += 1
            pointercol += 1
        else:
            break
    if count >= 4: return True

    pointerrow = row - 1
    pointercol = col - 1
    while pointercol >= 0 and pointercol < len(board[0]) and pointerrow >= 0 and pointerrow < len(board):
        if board[pointerrow][pointercol] == det:
            count += 1
            pointerrow -= 1
            pointercol -= 1
        else:
            break
    if count >= 4: return True

    # reset count and check the other direction- row & col are not both in/decrementing
    count = 1

    pointerrow = row - 1
    pointercol = col + 1
    while pointercol >= 0 and pointercol < len(board[0]) and pointerrow >= 0 and pointerrow < len(board):
        if board[pointerrow][pointercol] == det:
            count += 1
            pointerrow -= 1
            pointercol += 1
        else:
            break
    if count >= 4: return True

    pointerrow = row + 1
    pointercol = col - 1
    while pointercol >= 0 and pointercol < len(board[0]) and pointerrow >= 0 and pointerrow < len(board):
        if board[pointerrow][pointercol] == det:
            count += 1
            pointerrow += 1
            pointercol -= 1
        else:
            break
    if count >= 4: return True

    # if reach this point, return false (aka no winner)
    return False

def print_winner(board: list[list[int]]) -> None:
    print(*board, sep="\n")

    # use a nested for loop to check all coordinates of the board
    for row in range(len(board)):
        for col in range(len(board[0])):

            if board[row][col] == 1 and determine_winner(board, row,col, 1):
                print(f"player 1 wins")
                return # no need to continue searching
            
            if board[row][col] == 2 and determine_winner(board, row,col, 2):
                print(f"player 2 wins")
                return 
    
    # if reach this point, no winner
    print("no winner")
    return


def main() -> None:
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


if __name__ == "__main__":
    main()
