import random

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
    empty_cases_tr = []
    empty_cases = GET_EMPTY_CASES(board)
    for i in range(len(empty_cases)):
        empty_cases_tr.append(TRANSFORM_INDEX(empty_cases[i]))
        line, column = empty_cases_tr[len(empty_cases_tr) - 1]
        print(str(i+1) +' : [' + line + column + ']')
    return empty_cases_tr

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

def TRANSFORM_CASE(line, column):
    print(line, column)
    line = int(line)
    if column == 'A':
        column = 1
    if column == 'B':
        column = 2
    if column == 'C':
        column = 3

    print(line, column)
    return line, column

def PLAYERS_TURN(board):
    print("Chose where you will draw")
    empty_cases_tr = PRINT_EMPTY_CASES(board)
    target = int(input())
    line, column = TRANSFORM_CASE(empty_cases_tr[target - 1][0], empty_cases_tr[target - 1][1])
    PLACE_IN_BOARD(board,'O',line,column)
    PRINT_BOARD(board)

def BOT_RANDOM_TURN(board):
    empty_cases_tr = PRINT_EMPTY_CASES(board)
    target = random.choice(empty_cases_tr)
    line, column = TRANSFORM_CASE(target[0], target[1])
    PLACE_IN_BOARD(board,'X',line,column)
    PRINT_BOARD(board)

def GAME(board):
    for i in range(3):
        PLAYERS_TURN(board)
        BOT_RANDOM_TURN(board)

## Debugging
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# PRINT_BOARD(board)
#PRINT_BOARD(board)
# PRINT_EMPTY_CASES(board)
#PLAYERS_TURN(board)
GAME(board)