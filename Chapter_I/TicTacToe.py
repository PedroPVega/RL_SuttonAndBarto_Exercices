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

def GET_EMPTY_CASES(board):
    empty_cases = []
    for i in range (len(board)):
        if board[i] == ' ':
            empty_cases.append(i)
    return empty_cases

def PRINT_EMPTY_CASES(board):
    print("Available cases :")
    empty_cases = GET_EMPTY_CASES(board)
    for i in range(len(empty_cases)):
        line, column = TRANSFORM_INDEX(empty_cases[i])
        print('[' + line + column + ']')

def TRANSFORM_INDEX(case):
    line = case // 3
    column = case - 3*line
    line = str(line + 1)
    if column == 0:
        column = 'A'
    if column == 1:
        column = 'B'
    if column == 2:
        column = 'C'
    return line,column

def PLAYERS_TURN(board):
    PRINT_EMPTY_CASES(board)


## Debugging
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#PRINT_BOARD(board)
PLACE_IN_BOARD(board, 'X', 1, 1)
PLACE_IN_BOARD(board, 'O', 2, 2)
PLACE_IN_BOARD(board, 'X', 3, 3)
PRINT_BOARD(board)
PRINT_EMPTY_CASES(board)