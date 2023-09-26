board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


game_still_going = True
winner = None
current_player = "X"

def play_game():

  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    handling_turns(current_player)
    game_over()
    flip_player()
  
  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])
  print("\n")


def handling_turns(current_player):

  # Get position from player
  print(current_player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  
  valid = False
  while not valid:

  
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")
      
  board[position] = current_player
  display_board()

def game_over():
  check_for_winner()
  check_for_tie()


def check_for_winner():
  
  global winner
  
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  
  global game_still_going

  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  
  else:
    return None


def check_columns():
  
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  
  if column_1 or column_2 or column_3:
    game_still_going = False
  
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  else:
    return None


def check_diagonals():
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  else:
    return None


def check_for_tie():
  global game_still_going
  # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False

def flip_player():
  global current_player

  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"

#execution
play_game()