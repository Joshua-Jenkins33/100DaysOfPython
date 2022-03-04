# Scope

```py
################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")
  # prints 2

increase_enemies()
print(f"enemies outside function: {enemies}")
# prints 1

# Local Scope

def drink_potion():
  potion_strength = 2 # local scope; only accessible in this function
  print(potion_strength)

drink_potion() # this is equal to 2!
print(potion_strength) # this variable doesn't exist in this scope! It's not defined in this block of code!
```

The only difference between **local** and **global** scope is where you create or define your variables and functions.

```py
player_health = 10 # global scope; top level of the file; not within another function

def drink_potion():
  potion_strength = 2 # local variable
  print(player_health) # this is perfectly possible.
```

Global variables are available within functions (no matter how deep it gets nested) and outside of functions.

It also applies to functions and anything else you name.

## Namespace

Anything you give a name to has a namespace; that namespace is valid in certain scopes. This concept of scope applies to anything you name.

Nesting a function inside another turns it into a local scope.

# Block Scope

There is no such think as Block Scope in Python.

```py
if 3 > 2:
  a_variable = 10
```

These are still globally scoped.

```py
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy) # perfectly valid!
```

```py
game_level = 3
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # Not valid! new_enemy is now scoped to the function
```

If block/while loop/for loop or anything with indentation and colon, doesn't count as creating a separate local scope.

# How to Modify a Global Variable

```py
enemies = "Skeleton"

def increase_enemies():
  enemies = "Zombie" # we think we're setting the global enemies to 2, but what we're actually doing is creating a new variable called enemies with a local scope
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```

It is a bad idea to call your local and global variables the same name.

```py
enemies = 1

def increase_enemies():
  # enemies = 0 # this is what it *thinks* you are doing
  enemies += 1 # error: local variable 'enemies' defined in enclosing scope before assignment
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```

Explicitly say that you have a global variable set somewhere outside this function and *that's* the one you want to use *in* this function.

```py
enemies = 1

def increase_enemies():
  global enemies
  # enemies = 0 # this is what it *thinks* you are doing
  enemies += 1 # error: local variable 'enemies' defined in enclosing scope before assignment
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```
With *global* you cannot modify something that is global in a local scope.

You probably don't want to do this often; it's confusing and prone to bugs and errors (there's a reason it's hard to do).

Makes everything more fallible and easy to fail. Avoid modifying global scope. Read it, use it in your code; don't try to modify it in a function that has local scope.

How can you change the # of enemies without the global deal?

```py
enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
```

# Python Constants and Global Scope

Be careful with variables that have global scope; don't believe people that say you should *never* use global scope.

**Constants.** Something you create once and never want to change. Like the value of pi!
- Convention in Python is to make these names always UPPER CASE

```py
pi = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

def calc():
  TWITTER_HANDLE # this is a constant; we know to not modify it because of the caps!
```

