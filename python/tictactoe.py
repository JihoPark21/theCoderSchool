#Tic tac toe
#Using functions and array lists

board = []
for i in range(9):
   board.append(' ')

def printBoard():
   print()
   print(board[0] + '|' + board[1] + '|' + board[2])
   print('-+-+-')
   print(board[3] + '|' + board[4] + '|' + board[5])
   print('-+-+-')
   print(board[6] + '|' + board[7] + '|' + board[8])
   print()

def checkMove(spot):
   if board[spot] != ' ':
      return False
   return True

def checkWin(turn):
  if board[0] == turn and board[1] == turn and board[2] == turn:
    return True
  elif board[3] == turn and board[4] == turn and board[5] == turn:
    return True
  elif board[6] == turn and board[7] == turn and board[8] == turn:
    return True
  elif board[0] == board[4] == board[8] == turn:
    return True
  elif board[2] == board[4] == board[6] == turn:
    return True
  elif board[0] == board[3] == board[6] == turn:
    return True
  elif board[1] == board[4] == board[7] == turn:
    return True
  elif board[2] == board[5] == board[8] == turn:
    return True

move = 0
turn = 'X'

print("---------Tic Tac Toe---------")

while True:
   if move == 9:
      print("It\'s a tie")
      break

   print(turn + "\'s turn")
   spot = input("Where do you want to place your mark (0-8): ")
   spot = (int)(spot)

   while True:
      if checkMove(spot):
         board[spot] = turn
         break
      else:
         print("The move you entered is not allowed")
         spot = input("Enter a different spot (0-8): ")
         spot = (int)(spot)
   
   printBoard()

   if checkWin(turn):
      print(turn + " won")
      break

   if turn == 'X':
      turn = 'O'
   else:
      turn = 'X'
   
   move = move + 1