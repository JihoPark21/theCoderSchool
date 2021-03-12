import random

#Flip a coin a coin 3 times
#Keep track of how many times you've guessed right 

correct = 0

for i in range(3):
   #1 heads, 2 tails
   coin = random.randint(1,2)

   userGuess = input('1 for heads or 2 for tails: ')

   if (int)(userGuess) == coin:
      print("Good job")
      correct = correct + 1

print('You got %d correct guesses' % correct)