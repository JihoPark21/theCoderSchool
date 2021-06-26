import random

#Simple minesweeper game
#Hide two bombs, avoid digging in the wrong spot

bombBoard = []
gameBoard = []
mine = '💣'
not_mine = '⛏️'

for i in range(20):
   bombBoard.append(' ')
   gameBoard.append(' ')

def printBoard(theBoard):
   print()
   print(theBoard[0] + '|' + theBoard[1] + '|' + theBoard[2] + '|' + theBoard[3] + '|' + theBoard[4])
   print('-+-+-+-+-')
   print(theBoard[5] + '|' + theBoard[6] + '|' + theBoard[7] + '|' + theBoard[8] + '|' + theBoard[9])
   print('-+-+-+-+-')
   print(theBoard[10] + '|' + theBoard[11] + '|' + theBoard[12] + '|' + theBoard[13] + '|' + theBoard[14])
   print('-+-+-+-+-')
   print(theBoard[15] + '|' + theBoard[16] + '|' + theBoard[17] + '|' + theBoard[18] + '|' + theBoard[19])
   print()

def placeMines():
   spot1 = random.randint(0, 19)
   spot2 = random.randint(0, 19)
   #to avoid placing two mines in the same spot
   while spot1 == spot2:
      spot2 = random.randint(0, 19)
   bombBoard[spot1] = mine
   bombBoard[spot2] = mine

#This function will check if you can dig that spot, that spot has already been dug, or the spot has a bomb
#returns 1 if the move is good/allowed
#returns 2 if the move is not allowed
#returns 3 if the spot has a bomb
def checkSpot(spot):
   if bombBoard[spot] == ' ':
      gameBoard[spot] = not_mine
      bombBoard[spot] = not_mine
      return 1
   elif bombBoard[spot] == not_mine:
      return 2
   else:
      return 3

print("---------Simple Minesweeper---------")
print("There are two mines, avoid digging in those spots")

turn = 1
placeMines()

while turn < 19:
   print("Turn %d" % turn)
   digSpot = input("Which hole do you want to dig (0-19): ")
   digSpot = (int)(digSpot)

   state = checkSpot(digSpot)

   if state == 1:
      printBoard(gameBoard)
      turn = turn + 1
   elif state == 2:
      print("You can\'t dig there again")
   else:
      printBoard(bombBoard)
      print("BOOM!!!")
      break

if turn == 19:
   print("You did it!")