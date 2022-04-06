"""
Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.

Choose a difficulty. T ype 'easy' or 'hard': <input>

You have (hard: 5 | easy: 10) attempts remaining to guess the number.
Make a guess: <input>
Too <high|low>.
Guess again.
You have 4 attempts remaining to guess the number.
Make a guess: <input>
Too <high|low>.
Guess again.
You have 3 attempts remaining to guess the number.
...
You've run out of guesses, you lose.

Would you like to run again?

----------------------WIN----------------------
You got it! The answer was <answer>.
"""
from art import logo, win, lose
from random import randrange

def getDifficulty(game_difficulty: str):
  guesses = 0
  if game_difficulty == 'hard':
    guesses = 5
  elif game_difficulty == 'easy':
    guesses = 10
  return guesses
  

def randomNumber():
  """
  This gets a random number between 1 and 100; it is the game winning number!
  """
  return randrange(1,101)

def gamePlay(number_of_guesses: int, answer: int):
  """
  Compares the guess against the winning number

  Args:
      guesses (int): The number of guesses a user gets
      answer (int): The game winning number
  """

  while number_of_guesses > 0:
    print(f"You have {number_of_guesses} attempts remaining to guess the number.")
    player_guess: int = int(input("Make a guess: "))
    if player_guess > answer:
      number_of_guesses -= 1
      print( "Too high.")
    elif player_guess < answer: 
      number_of_guesses -= 1
      print("Too low.")
    else:
      print(win)
      print(f"You got it! The answer was {answer}.")
      number_of_guesses = 0

  if number_of_guesses == 0 and player_guess != answer:
    print(lose)



keepPlaying: bool = True

while keepPlaying == True:
  print(logo)
  print("I'm thinking of a number between 1 and 100.")

  difficulty: str = input("Choose a difficulty. Type 'easy' for more guesses or 'hard' for fewer guesses: ")

  gamePlay(getDifficulty(difficulty), randomNumber())

  again = input("Would you like to play again? Type 'y' or 'n': ")
  if again == 'n':
    print("Come play again soon!")
    keepPlaying = False

