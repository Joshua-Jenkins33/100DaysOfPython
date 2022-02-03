# IMPORT MODULES
from art import logo, vs
from game_data import data
from random import randrange

# GENERATE RANDOM NUMBER AND USE IT TO GET A RANDOM FACT
def getRandomFact(data: list):
  """Gets a random item from the data list

  Args:
      data (list): Contains the data we use to run our game

  Returns:
      dict: A single dictionary item from our data list
  """
  rando = randrange(0,len(data))
  return data[rando]

# DETERMINE THE RIGHT ANSWER
def rightAnswer(a: dict, b: dict):
  if a['follower_count'] > b['follower_count']:
    return a
  elif a['follower_count'] < b['follower_count']:
    return b
  else:
    return a

# PRINT DICTIONARY TO STRING
def printTheDict(the_dict: dict, a_or_b: str):
  if a_or_b == 'a':
    print(f"Compare A: {the_dict['name']}, a {the_dict['description']}, from {the_dict['country']}.")
  else:
    print(f"Compare B: {the_dict['name']}, a {the_dict['description']}, from {the_dict['country']}.")

# PROMPT THE USER FOR WHAT THEY THINK THE ANSWER IS
def userGuess(option1: dict, option2: dict, answer: dict, score: int):
  guess = input("\nWhich do you think has more followers? 'a' or 'b'?: ")
  if guess == 'a':
    if option1['name'] == answer['name']:
      score +=1 
      print("Congratulations! That's right!")
      return([1,score,answer])
    else:
      print(f"Sorry. You lose. Your final score was {score}.")
      return([0,score,answer])
  elif guess == 'b':
    if option2['name'] == answer['name']:
      score +=1 
      print("Congratulations! That's right!")
      return([1,score, answer])
    else:
      print(f"Sorry. You lose. Your final score was {score}.")
      return([0,score, answer])

# PRINT STARTER INFO

a = getRandomFact(data)
end_game = False
score = 0

while not end_game:
  print(logo)
  b = getRandomFact(data)
  print(f"Your score is: {score}.")
  printTheDict(a, 'a')
  print(vs)
  printTheDict(b, 'b')
  guess_results = userGuess(a, b, rightAnswer(a, b), score)
  score = guess_results[1]
  should_continue = guess_results[0]
  a = guess_results[2]

  if should_continue == 0:
    end_game = True
  

# ASK THE USER IF THEY WANT TO PLAY

# TO START, PULL OUT TWO RANDOM BITS FROM GAME_DATA

# PROMPT THE USER TO SELECT ONE

# COMPARE VALUESb

## DID THE USER SELECT THE RIGHT ONE? INCREMENT THE SCORE AND PULL A SINGLE NEW BIT FROM GAME_DATA

## MAKE SURE THE RIGHT BIT FROM LAST TIME IS NOW THE "A" BIT

## DID THE USER SELECT THE WRONG ONE? TOTAL THE SCORE AND END THE GAME