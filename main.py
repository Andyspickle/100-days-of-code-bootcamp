#Number Guessing Game Objectives:
import random
from replit import clear
from art import logo

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

introduction = """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100."""

# def check_guess(user_guess, random_number):
#   if user_guess == 0:
    
#   elif user_guess == random_number:
#     print(f"You got it! The answer was {random_number}")
  # elif user_guess > random_number:
  #   print("Too high.")
  #   print("Guess again.")
  # elif user_guess < random_number:
  #   print("Too low.")
  #   print("Guess again.")

def set_difficulty(diffculty):
  """Set the number of lives based on the difficulty"""
  if diffculty.lower() == "easy":
    return 10
  elif diffculty.lower() == "hard":
    return 5


def play_game():
  print(logo)
  print(introduction)
  user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  user_lives = set_difficulty(user_choice)
  random_number = random.randint(1, 100)
  
  print(random_number)

  game_over = False


  while not game_over:
    print(f"You have {user_lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    # check_guess(user_guess, random_number)

    if user_guess < 1 or user_guess > 100:
      print("Invalid number, try again.")
    elif user_guess == random_number:
      game_over = True
      print(f"You got it! The answer was {random_number}")
    elif user_guess > random_number:
      print("Too high.")
      print("Guess again.")
      user_lives -= 1
    elif user_guess < random_number:
      print("Too low.")
      print("Guess again.")
      user_lives -= 1

    if user_lives == 0:
      game_over = True
      print("You've run out of guesses, you lose.")

    
    
    
    

  # print(compare_numbers(user_guess, rand))
    
    
      
  
while input("Do you want to play the guessing game? 'y' or 'n': ") == "y":
  clear()
  play_game()



  
  