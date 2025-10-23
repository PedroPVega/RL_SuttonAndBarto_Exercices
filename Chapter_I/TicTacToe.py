import random

board_config_1 = [0,1,2]
board_config_2 = [3,4,5]
board_config_3 = [6,7,8]
board_config_4 = [0,4,8]

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
    for i in range(4):
        PLAYERS_TURN(board)
        BOT_RANDOM_TURN(board)
        CHECK_VICTORY(board, 'X', 'O')

def TURNBOARD_CLOCKWISE(ref_board):
    new_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    new_board[0] = ref_board[6]
    new_board[1] = ref_board[3]
    new_board[2] = ref_board[0]
    new_board[3] = ref_board[7]
    new_board[4] = ref_board[4]
    new_board[5] = ref_board[1]
    new_board[6] = ref_board[8]
    new_board[7] = ref_board[5]
    new_board[8] = ref_board[2]
    return new_board

def CHECK_VICTORY(board, player, bot):
    '''
    config1.      config2.      config3.      config4. 
    X X X         ? ? ?         ? ? ?         X ? ?
    ? ? ?         X X X         ? ? ?         ? X ?
    ? ? ?         ? ? ?         X X X         ? ? X
    '''
    possible_configs = [board_config_1, board_config_2, board_config_3, board_config_4]
    for i in range(4): ## number of possible rotations
        for j in range(4): ## number of configs
            if board[possible_configs[j][0]] == board[possible_configs[j][1]] and board[possible_configs[j][1]] == board[possible_configs[j][2]]:
                if board[possible_configs[j][0]] == player:
                    print("the player :",player,"wins !")
                    return
                elif board[possible_configs[j][0]] == bot:
                    print("the player :",bot,"wins !")
                    return
        board = TURNBOARD_CLOCKWISE(board)
    print("neither player wins!")
    return


## Debugging
# board1 = ['0','1','2','3','4','5','6','7','8']
board2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# board1 = TURNBOARD_CLOCKWISE(board1)
#PRINT_BOARD(board)
# PRINT_EMPTY_CASES(board)
#PLAYERS_TURN(board)
GAME(board2)

def TEST_VICTORY_CHECK_FUNC():
    # Testing Victory Check
    board3 = ['X','X','X',' ','O',' ',' ','O',' ']
    board4 = ['X',' ',' ','X','O',' ','X','O',' ']
    board5 = ['O',' ',' ','O','O',' ','O','O',' ']
    board6 = ['X',' ',' ','O','X',' ',' ','O','X']
    board7 = ['X',' ','O','X','O',' ','O','X','X']
    board8 = [' ','X',' ','O','X',' ','O','X',' ']
    test_boards = [board2, board3, board4, board5, board6, board7, board8]

    for j in range(len(test_boards)):
        PRINT_BOARD(test_boards[j])
        CHECK_VICTORY(test_boards[j], 'X', 'O')
        print("-----------------------------------------")
