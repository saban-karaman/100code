import random
from keep_number_logo import logo
print(logo)
difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
number = random.randint(1,100)
make_guess = 1
def guess():
  global number
  global make_guess 
  make_guess = int(input("make a guess: "))
  if number == make_guess:
    print("Congrat! you are awesome")
  elif number < make_guess:
    print("Too high.")
  else:
    print("Too low.")
def easy():
  global number
  global make_guess
  i = 0
  while make_guess != number and i != 10:
      guess()
      i += 1
      if make_guess != number:
        print(f"You have {10 - i} attemp remainig.")
  if make_guess == number:
      print("bravo")      
  elif i == 10:
    print("You Lose :D")
def hard():
  global number
  global make_guess
  i = 0
  while make_guess != number and i != 5:
      guess()
      i += 1
      if make_guess != number:
        print(f"You have {5 - i} attemp remainig.")
  if make_guess == number:
      print("bravo")      
  elif i == 5:
    print("You Lose :D")
if difficulty == "easy":
  easy()
else:
  hard() 