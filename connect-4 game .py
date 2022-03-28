board = [[' 'for spot in range(7)] for row in range(6)]

def display_board(board):
    print("  1    2    3    4    5    6    7")   
    for row in board:
        print(row)

####################################################################

def is_winner(board , num):
    for row in board :                         #horizontal check win
        for i in range(4):
            if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                print(f"player{num} wins")
                return "end"

    for i in range(7) :                         #vertical check win
        for j in range(3) :
            if board[j][i] != ' ' and board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i]:
                print(f"player{num} wins")
                return "end"

    for i in range(3):                          #diagonal left-high-corner : right-low-corner check win
        for j in range(4):
            if board[i][j] != ' ' and board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                print(f"player{num} wins")
                return "end"
    
    for i in range(3):                           #diagonal right-high-corner : left-low-corner check win
        for j in range(-1 , -5 ,-1):
            if board[i][j] != ' ' and board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]:
                print(f"player{num} wins")
                return "end"

####################################################################

def is_draw(board):                                      #check draw
    if ' ' not in board[0]:
        print("Game Draw")
        return "end"

####################################################################

def column_relay(symbol , board , colmun , num):        #put the new item above the old item
    for i in range(5,-1 , -1) :
        if board[i][colmun] == ' ' :
            board[i][colmun] = symbol
            display_board(board)
            break
    else :
        print("unavailable colmun")
        player_input_check(num)

####################################################################

def player_input_check(num):                #handling player's input and check it
    player_input = input(f"player{num} enter column number in range 1-7 :")
    if player_input.strip().lower() == 'q':
        print("see you again")
        return "quit"
        
    elif player_input.isnumeric() and int(player_input) > 0 and int(player_input) <= 7:
        if num == 1 :
            symbol ='X'
        elif num ==2 :
            symbol = 'O'
        column_relay(symbol, board , int(player_input)-1 , num)
    
    else:
        print("wrong value, please enter a valid number")
        player_input_check(num)

####################################################################

def board_update():                              #update game state
    while True :
        the_input = player_input_check(1)
        if the_input == "quit" :
            return -1
        if is_winner(board , 1) == "end" :
            return -1
    
        the_input = player_input_check(2)
        if the_input == "quit" :
            return -1
        if is_winner(board , 2) == "end" :
            return -1

        if is_draw(board) == "end" :
            return -1

####################################################################

def run_game():                                        #run the game
    while True:
        display_board(board)
        if board_update() == -1 :
            break

####################################################################

run_game()