import random

#random quiz program
#Quiz will have 5 questions
#Use lots of functions

def addition(x, y):
   return x + y

def subtraction(x, y):
   return x - y

def multiplication(x, y):
   return x * y

def division(x, y):
   if y == 0:
      return 'You can\'t divide by 0'
   else:
      return round((float)(x) / (float)(y), 2)

print('Let\'s take a quiz')
print("Addition quiz (+)\n" +
      "Subtraction quiz (-)\n" +
      "Multiplication quiz (*)\n" +
      "Division Quiz (/) !Round to the second decimal place")

score = 0
userQuiz = input("Which quiz would you like to take: ")

for i in range(5):
   x = random.randint(1, 10)
   y = random.randint(1, 10)

   if userQuiz == "+":
      print("%d + %d = " % (x, y), end = "")
      userAnswer = input()
      answer = addition(x,y)
      if (int)(userAnswer) == answer:
         print("Correct")
         score = score + 1
      else:
         print("Incorrect. Answer was %d" % answer)
   elif userQuiz == "-":
      print("%d - %d = " % (x, y), end = "")
      userAnswer = input()
      answer = subtraction(x, y)
      if (int)(userAnswer) == answer:
         print("Correct")
         score = score + 1
      else:
         print("Incorrect. Answer was %d" % answer)
   elif userQuiz == "*":
      print("%d * %d = " % (x, y), end = "")
      userAnswer = input()
      answer = multiplication(x, y)
      if (int)(userAnswer) == answer:
         print("Correct")
         score = score + 1
      else:
         print("Incorrect. Answer was %d" % answer)
   else:
      print("%d / %d = " % (x, y), end = "")
      userAnswer = input()
      answer = division(x, y)
      if (float)(userAnswer) == answer:
         print("Correct")
         score = score + 1
      else:
         print("Incorrect. Answer was %.2f" % answer)

print("You got %d/5" % score)