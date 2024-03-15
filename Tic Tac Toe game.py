# Tic Tac Toe


board = ["_","_","_",
         "_","_","_",
         "_","_","_",]

def game_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


current_player = "X"

# Game going on

game_still_going = True

def handle_players():

  print()
  print (current_player + "'s turn.")
  print ()

  position = input("Choose a digit between 1-9: ")
  print ()

  valid = False

  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position = input(" Please choose a valid digit between 1-9: ")
        print ()

    position = int (position) - 1

    if board[position] == "_":
      valid = True
    else:
      print("This one's taken.Please choose another")
      print()
  board[position] = current_player
  game_board()

def check_if_game_over():

  check_if_win()

  check_if_tie()

def check_if_win():

  global winner

  #check rows

  row_winner = check_rows()

  # check columns

  column_winner = check_columns()

  #check diagonals

  diagonal_winner = check_diagonals()

  if row_winner:

    # we have a winner

    winner = row_winner

  elif column_winner:

    # we have a winner

    winner = column_winner

  elif diagonal_winner:

    # we have a winner

    winner = diagonal_winner
  
  else:

    # It's a Tie 
     winner = None

  return

def check_rows():

  global game_still_going

  row_1 = board[0] == board[1] == board[2] != "_"
  row_2 = board[3] == board[4] == board[5] != "_"
  row_3 = board[6] == board[7] == board[8] != "_"

  if row_1 or row_2 or row_3:
    game_still_going = False

  if row_1:
    return board[0]
  if row_2:
    return board[3]
  if row_3:
    return board[6]

  return

def check_columns():

  global game_still_going

  column_1 = board[0] == board[3] == board[6] != "_"
  column_2 = board[1] == board[4] == board[7] != "_"
  column_3 = board[2] == board[5] == board[8] != "_"

  if column_1 or column_2 or column_3:
    game_still_going = False

  if column_1:
    return board[0]
  if column_2:
    return board[1]
  if column_3:
    return board[2]

  return

def check_diagonals():

  global game_still_going

  diagonal_1 = board[0] == board[4] == board[8] != "_"
  diagonal_2 = board[2] == board[4] == board[6] != "_"
  
  if diagonal_1 or diagonal_2 :
    game_still_going = False

  if diagonal_1:
    return board[0]
  if diagonal_2:
    return board[2]
 
  return

def check_if_tie():

  global game_still_going

  if "_" not in board:
    game_still_going = False
  return

def flip_players():

  global current_player

  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"

  return

def play_game():

  game_board()
  print()

  while game_still_going:
    
    handle_players()

    check_if_game_over()

    flip_players()

  # how the game will end

  if winner == "X" or winner == "O":
    print()
    print (winner + " wins.")
  elif winner == None:
    print()
    print ("It's a Tie.")

print("Tic Tac Toe Game...")
print()
print("Wanna Play...?")
print()
a = input("Reply with just y or n: ")
val = False

while not val:
    while a not in ['y', 'Y', 'n', 'N']:
        print()
        print("Bruh your keyboard doesn't work??")
        print()
        a = input("Reply with just y or n: ")
    if a == 'y' or a == 'Y':
        val = True
        print()
        play_game()
    elif a == 'n' or a == 'N':
        val = True
        print()
        print()
        print()
        print()
        print()
        b = input("Here is a code message in russian for you... 'Ты глупый :)' ")

if a in ['y', 'Y']:
    print()
    print("Wanna Play One More Time..?")
    print()
    ans = input("Reply with y or n : ")
    mat = False
    while not mat:
        while ans not in ['y', 'Y', 'n', 'N']:
            print()
            print("Bruh your keyboard doesn't work??")
            print()
            ans = input("Reply with just y or n: ")
        if ans in ['y', 'Y', 'n', 'N']:
            mat = True
            while ans in ['y', 'Y']:
                board = ["_","_","_",
                         "_","_","_",
                         "_","_","_",]
                game_still_going = True
                print()
                play_game()
                print()
                print("Wanna Play One More Time..?")
                print()
                ans = input("Reply with y or n : ")
            else:
                print()
                input("Yoy are a lovely person\nHave a Good day\nPress Enter to quit...:)")