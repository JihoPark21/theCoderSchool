import random

#hangman

wordbank = ['coder', 'dog', 'school', 'cat', 'think']
word = wordbank[random.randint(0, len(wordbank))]

lives = 6
blanks = []

for letter in word:
   blanks.append('_')

#function for checking blanks
#if there are no more '_' left return True
def checkBlanks(blank):
   for letter in blank:
      if letter == '_':
         return False
   return True

while True:
   #Tell the user how many lives they have left
   print("You have %d lives" % lives)

   #printing out the blanks
   for char in blanks:
      print(char, end = ' ')
   print()

   #You lose if you have 0 lives left
   if lives == 0:
      print("You lose")
      break

   #if our checkBlanks function returns True
   if checkBlanks(blanks):
      print("You win")
      break

   #Handling input and lives
   letterIsSeen = False
   userGuess = input("Guess a letter: ")
   userGuess = userGuess.lower()

   for i in range(len(word)):
      if word[i] == userGuess:
         blanks[i] = userGuess
         letterIsSeen = True
   
   if letterIsSeen == False:
      lives = lives - 1