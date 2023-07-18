from replit import clear
from art import logo, vs
from game_data import data
import random

# Function to check user's input against correct answer

def check_answer(guess, answer, score):
  """Checks answer against guess and returns the current score."""
  if guess == answer:
    print(f"You're right! Current score: {score + 1}")
    return score + 1
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, you're wrong. Final score: {score}")
    return score

def format_data(account):
  """Formats the data in a printable version"""
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"

def game():
  print(logo)
  # Choose two random keys from the game data file
  choice_a = random.choice(data)
  choice_b = random.choice(data)
  if choice_a == choice_b:
    choice_b = random.choice(data)
  
  
  answer = ""
   
  if choice_a['follower_count'] > choice_b['follower_count']:
    answer = 'a'
  else:
    answer = 'b'

  # Repeat the guessing functionality until they get it wrong
  score = 0
  guess = answer
  while guess == answer:
    
    ##Ask user for who has more followers, A or B?
    print(f"Pssst, the correct answer is {answer}")
    print(f"Compare A: {format_data(choice_a)}.")
    print(vs)
    print(f"Against B: {format_data(choice_b)}.")
    guess = input("Who has more follows? 'A' or 'B': ").lower()
    clear()
    print(logo)
    ##If right, replace A with B, and generate another answer for B

    score = check_answer(guess, answer, score)
    choice_a = choice_b
    choice_b = random.choice(data)

game()

