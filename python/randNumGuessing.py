import random

#Make a random number
#Try to have the user guess that random number

randnum = random.randint(1, 10)

#print(randnum)

while True:
   userInput = input("Guess a random number 1-10: ")
   if (int)(userInput) == randnum:
      break

print("The random number was %d" % randnum)