import random

#rock paper scissors
#if-elses

#1 - rock, 2 - paper, 3 - scissors

playerWins = 0
computerWins = 0

print("---------Rock Paper Scissors---------")
print("Play against a computer. First to 3 wins.")


while playerWins < 3 and computerWins < 3:
   print("Enter 1 for Rock")
   print("Enter 2 for Paper")
   print("Enter 3 for Scissors")

   print("\nPlayer wins: %d   Computer wins: %d\n" % (playerWins, computerWins))

   userinput = input("What would you like to play (1-3): ")
   userinput = (int)(userinput)
   print()

   compPlays = random.randint(1,3)

   if userinput == 1:
      if compPlays == 1:
         print("Tie. Both played rock")
      elif compPlays == 2:
         print("Computer wins. Paper beats rock")
         computerWins = computerWins + 1
      else:
         print("Player wins. Rock beats scissors")
         playerWins = playerWins + 1
   elif userinput == 2:
      if compPlays == 1:
         print("Player wins. Paper beats rock")
         playerWins = playerWins + 1
      elif compPlays == 2:
         print("Tie. Both played paper")
      else:
         print("Computer wins. Scissors beats paper")
         computerWins = computerWins + 1
   else:
      if compPlays == 1:
         print("Computer wins. Rock beats scissors")
         computerWins = computerWins + 1
      elif compPlays == 2:
         print("Player wins. Scissors beats paper")
      else:
         print("Tie. Both played paper")
   
   print("\n-------------------------------------\n")

if playerWins == 3:
   print("You won")
else:
   print("Computer won")