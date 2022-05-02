import random
from art import logo
print(logo)
print("Welcome  to the Number guessing game!")
print("guess a number between 1 and 100")

def easy():
  count=10
  random_number=random.randint(1,100)

  while count>0:
    guess_num = int(input("Make a guess"))
    if random_number==guess_num:
      print("correct guess")
      count=0
    elif random_number+10>guess_num>random_number:
      print("high")
    elif guess_num>random_number+10:
      print("too high")
    elif random_number-10<guess_num<random_number:
      print("low")
    elif guess_num<random_number-10:
      print("too low")
    count=count-1
  print(f"correct number is {random_number}")

def hard():
  count=5
  random_number=random.randint(1,100)

  while count>0:
    guess_num = int(input("Make a guess"))
    if random_number==guess_num:
      print("correct guess")
      count=0
    elif random_number+10>guess_num>random_number:
      print("high")
    elif guess_num>random_number+10:
      print("too high")
    elif random_number-10<guess_num<random_number:
      print("low")
    elif guess_num<random_number-10:
      print("too low")
    count=count-1
  print(f"correct number is {random_number}")

choose_difficulty = input("choose a difficulty type 'easy' or 'hard':").lower()
if choose_difficulty == "easy":
  easy()
elif choose_difficulty == "hard":
  hard()