from higher_lower_art import logo, vs
from higher_lower_game_data import data
from random import randint
import random
# asign_a = random.choice(data)
#print(f"{asign_a['name']}, {asign_a['description']}, {asign_a['country']}")
# asign_b = data[random.randint(0,len(data))]
# print(asign_b)
# print(f"{asign_b['name']}, {asign_b['description']}, {asign_b['country']}")

def asign():
  global data
  a = random.randint(0,len(data))
  x = data[a]
  del(data[a])
  return x
# def compare(a, b):
#   if a["follower_count"] > b["follower_count"]:
#     a = a
#     b = asign()
#     i += 1
#     print(f"You are right! Current score : {i}")
#   elif a["follower_count"] < b["follower_count"]:
#     prin("You Lose!")
print(logo)
i = 0
asign_a = asign()
asign_b = asign()
while True:
    print(f"Compare A: {asign_a['name']}, {asign_a['description']}, {asign_a['country']}")
    print(vs)
    print(f"Compare B: {asign_b['name']}, {asign_b['description']}, {asign_b['country']}")
    who = input("Who has more followers? Type A or Type B :").upper()
    if who == "A":
        if asign_a["follower_count"] > asign_b["follower_count"]:
          asign_a = asign_a
          asign_b = asign()
          i += 1
          print(f"You are right! Current score : {i}")
        elif asign_a["follower_count"] < asign_b["follower_count"]:
          print(f"Sorry, you lose. Your Score {i}")
          break
    elif who == "B":
        if asign_b["follower_count"] > asign_a["follower_count"]:
          asign_a = asign_b
          asign_b = asign()
          i += 1
          print(f"You are right! Current score : {i}")
        elif asign_b["follower_count"] < asign_a["follower_count"]:
          print(f"Sorry, you lose. Your Score {i}")
          break
    elif i == 48:
      print("you are a Legend 😎")
      break