game_board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]


title = r'''
 _   _      _             _             
| | (_)    | |           | |            
| |_ _  ___| |_ __ _  ___| |_ ___   ___ 
| __| |/ __| __/ _` |/ __| __/ _ \ / _ \
| |_| | (__| || (_| | (__| || (_) |  __/
 \__|_|\___|\__\__,_|\___|\__\___/ \___|
'''


def play_for_x(game_board):
    while True:
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))

        if game_board[row-1][column-1] == "":
            game_board[row-1][column-1] = 'X'
            for row in game_board:
                print(row)
            return False
        else:
            print("The cell you specified is full, try again!")

def play_for_o(game_board):
    while True:
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))

        if game_board[row-1][column-1] == "":
            game_board[row-1][column-1] = 'O'
            for row in game_board:
                print(row)
            return False
        else:
            print("The cell you specified is full, try again!")

def check_game(game_board, player):
    # Checking for rows
    for row in game_board:
        if all(cell == player for cell in row):
            print(f"Player {player} wins!")
            return True
        

    # Checking for columns
    for col in range(3):
        if all(game_board[row][col] == player for row in range(3)):
            print(f"Player {player} wins!")
            return True
       

    # Checking for diagonals
    if all(game_board[i][i] == player for i in range(3)):
        print(f"Player {player} wins!")
        return True
   

    if all(game_board[i][2-i] == player for i in range(3)):
        print(f"Player {player} wins!")
        return True
  

def game():
    game = True
    print(title)
    for row in game_board:
        print(row)
    while game:
        
        print("Play for X")
        play_for_x(game_board)
        if check_game(game_board, 'X') == True:
            game = False

        print("Play for O")
        play_for_o(game_board)
        if check_game(game_board, 'O') == True:
            game = False



game()
        

    
