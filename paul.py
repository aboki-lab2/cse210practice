''''''''''''''''''''''''''''
Tic-Tac-Toe: A Solution1
'''''''''''''''''''''''''''''''''
# This is where our game will be held
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# let us know who emerges the winner
winner = None

# This will indicate if our game is still running
game_still_running = True


# Who is our current player
active_player = "X"


# Welcome to the game of tic tac
def main ():

  # Show the initial game board
  display_board()

  # Loop continues till game stops (winner or tie)
  while game_still_running:

    # Each of the players(X AND O will take turn to play)
    random(active_player)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()
  
  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# This is the game board. The figures to press and the board will diaplay empty with dashes that will be populated with an x or o
def display_board():
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}" + "               1 | 2 | 3")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}" + "               4 | 5 | 6")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}" + "               7 | 8 | 9")
    print()


# Random player
def random (player):

  # Get position from player
  print(player + "'s turn.")
  position = input(" Please kindly select a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Please kindly select a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # what happens when you select the wrong figure
    if board[position] == "-":
      valid = True
    else:
      print("Sorry you made a wrong choice. Try again later.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()


# game outcome
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check out the winner
def check_for_winner():
  # Set global variables
  global winner
  # How to win(row, column and diagonal)
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
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
  # Set global variables
  global game_still_running
  # Check rows 1-3
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # check if any of the rows has a win
  if row_1 or row_2 or row_3:
    game_still_running = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return  no winner emerged
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_running
  # Check the columns
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any of the columns has a win indicate
  if column_1 or column_2 or column_3:
    game_still_running = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return no winner emerged
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_running
  # chech if the of the rows that make up the diagonal lines have same figure
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If there is a match a winner has emerged
  if diagonal_1 or diagonal_2:
    game_still_running = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if no winner emerged
  else:
    return None


# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_still_running
  # If board is full
  if "-" not in board:
    game_still_running = False
    return True
  # Else there is no tie
  else:
    return False


# Flip the active player from O to X, or X to O
def flip_player():
  # Global variables we need
  global active_player
  # If the active player was O, make it X
  if active_player == "O":
    active_player = "X"
  # Or if the active player was O, make it X
  elif active_player == "X":
    active_player = "O"

if __name__ == "__main__":
    main()