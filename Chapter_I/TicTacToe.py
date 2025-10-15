def PRINT_BOARD(board):
    if len(board) != 9:
        print("Error : no board found")
        return
    print("    A   B   C  ")
    print("  ╬═══╬═══╬═══╣")
    print("1 ║",board[0],"║",board[1],"║",board[2],"║")
    print("  ╬═══╬═══╬═══╣")
    print("2 ║",board[3],"║",board[4],"║",board[5],"║")
    print("  ╬═══╬═══╬═══╣")
    print("3 ║",board[6],"║",board[7],"║",board[8],"║")
    print("  ╩═══╩═══╩═══╝")

def PLACE_IN_BOARD(board, letter, line, column):
    pos = 3*line + column - 4
    board[pos] = letter
## Debugging
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#PRINT_BOARD(board)
PLACE_IN_BOARD(board, 'X', 1, 1)
PLACE_IN_BOARD(board, 'O', 2, 2)
PLACE_IN_BOARD(board, 'X', 3, 3)
PRINT_BOARD(board)