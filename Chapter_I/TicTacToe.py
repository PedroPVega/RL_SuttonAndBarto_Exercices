board = ['A','B','C',' ',' ',' ',' ',' ',' ']
# ╬ ║ ╣ ═ ╠ ╦ ╧ ╗╔ ╝╚
def PRINT_BOARD(board):
    if len(board) != 9:
        print("Error : no board found")
        return
    print("╔═══╦═══╦═══╗")
    print("║",board[0],"║",board[1],"║",board[2],"║")

PRINT_BOARD(board)