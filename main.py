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
EASY_MODE = 10
HARD_MODE = 5
TURNS = 0

introduction = """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100."""

def check_answers(guess, answer, turns):
  """Check the answer against the guess, returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  """Set the number of turns based on the difficulty"""
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty.lower() == "easy":
    return EASY_MODE
  elif difficulty.lower() == "hard":
    return HARD_MODE
    


def start_game():
  print(logo)
  print(introduction)
  answer = random.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")
  turns = set_difficulty()
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answers(guess, answer, turns)

    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
      
    

def play_game():
  print(logo)
  print(introduction)
  magic_number = random.randint(1, 100)
  print(f"Pssst, the correct answer is {magic_number}")
  user_lives = set_difficulty()
  print(f"You have {user_lives} attempts remaining to guess the number.")

  game_over = False


  while not game_over:
    print(f"You have {user_lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    # check_guess(user_guess, random_number)

    if user_guess < 1 or user_guess > 100:
      print("Invalid number, try again.")
    elif user_guess == magic_number:
      game_over = True
      print(f"You got it! The answer was {magic_number}")
    elif user_guess > magic_number:
      print("Guess again.")
      user_lives -= 1
    elif user_guess < magic_number:
      print("Too low.")
      print("Guess again.")
      user_lives -= 1

    if user_lives == 0:
      game_over = True
      print("You've run out of guesses, you lose.")

    
    
    
    

  # print(compare_numbers(user_guess, rand))
    
    
      
  
while input("Do you want to play the guessing game? 'y' or 'n': ") == "y":
  clear()
  start_game()



  
  