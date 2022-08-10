import random
from art import logo
from art import vs
from replit import clear
from game_data import data
def get_account():
  return random.choice(data)

def format(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  print(f"{name}, a {description}, from {country}.")

def compare(guess,a_followers,b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def play_game():
  print(logo)
  score = 0
  game_continue = True
  account_a = get_account()
  account_b = get_account()
  while game_continue:
    account_a = account_b
    account_b = get_account()
    while account_a == account_b:
      account_b = get_account()
      print(f"Compare: A {format(account_a)}")
      print(vs)
      print(f"Against: B {format(account_b)}")
      guess = input("Who has more followers A or B\n").lower()
      a_followers = account_a["follower_count"]
      b_followers = account_b["follower_count"]
      is_correct = compare(guess,a_followers,b_followers)
      clear()
      print(logo)
      if is_correct:
        score += 1
        print(f"You're right. Current score: {score}")
      else:
        game_continue = False
        print(f"Sorry thats wrong. Final score: {score}")


play_game()
        