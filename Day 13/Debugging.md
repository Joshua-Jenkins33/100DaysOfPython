# Debugging

Removing bugs from your code. How to find bugs and get rid of them.

1. Describe the Problem
  - Untangle the problem to make sense of what is going on.
2. Reproduce the Bug
3. Play Computer
4. Fix the Errors
5. Print is Your Friend
6. Use a Debugger
7. Take a Break
  - Staring at the code... it's not going to tell you the solution; have a cup of tea, nap, come back to it tomorrow; things sometimes become more obvious
8. Ask a Friend
9. Run Often
  - That is, your code.
10. Ask StackOverflow

## Example 1

1. Describe the Problem:
  - What is the for-loop doing?
    - The for-loop is running through a range of numbers, from 1 to 19
  - When is the function meant to print *"You got it"*?
    - It's meant to print *"You got it"* when `i == 20` which never happens in this case

```py
def my_function():
  for i in range(1, 20): # an assumption that range reaches 20
    for i == 20:
      print("You got it")
my_function()

# This doesn't return anything! Oops! Range doesn't include that number; it gets a number between 1 and 19!
def my_function():
  for i in range(1, 21): # this would fix the bug!!
    for i == 20:
      print("You got it")
my_function()

```

## Example 2

```py
############DEBUGGING#####################

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) # ❶ will never get called because arrays are 0 based; our random integer will never be 0. ❻ is in dice_imgs[5] spot, not dice_imgs[6] spot; our array isn't that long, so it's out of range
print(dice_imgs[dice_num])

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = 6 # use this for debugging!
dice_num = randint(0,5)
print(dice_imgs[dice_num]) 
```

## Example 3
```py
# Play Computer
# 1994 returns nothing!!
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
```

## Example 4
```py
# Fix the Errors
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.") # expects an indented block
# execution is a TypeError '>' not supported between instance of 'str' and 'int'

# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")
```

## Example 5

```py
#Print is Your Friend
pages = 0
print(f"Pages: {pages}")
word_per_page = 0
print(f"Words per page: {word_per_page}")
pages = int(input("Number of pages: "))
print(f"Pages after input: {pages}")
word_per_page == int(input("Number of words per page: ")) # there's a conditional operator, not an assignment one; == should be =
print(f"Words per page after input: {word_per_page}")
total_words = pages * word_per_page
print(f"Total Words: {total_words}")

# =======================================================================================
# FIXED CODE
# =======================================================================================
pages = 0
print(f"Pages: {pages}")
word_per_page = 0
print(f"Words per page: {word_per_page}")
pages = int(input("Number of pages: "))
print(f"Pages after input: {pages}")
word_per_page = int(input("Number of words per page: ")) # there's a conditional operator, not an assignment one; == should be =
print(f"Words per page after input: {word_per_page}")
total_words = pages * word_per_page
print(f"Total Words: {total_words}")
```

## Example 6

```py
#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item) # This should be indented! Needs to happen *inside* the loop
  print(b_list)

mutate([1,2,3,5,8,13])
```
