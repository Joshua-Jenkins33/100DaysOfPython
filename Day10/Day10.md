# Day 10 Functions with Outputs

Building a Calculator application!

## More Functions!!

A review below!

```py
def my_function():
    #Do this
    #Then do this
    #Finally do this
```

Second thing we worked over!

```py
def my_function(something):
    #Do this with something
    #Then do this
    #Finally do this
```

### Functions with Outputs

```py
def my_function():
    result = 3*2
    return result
    # output = my_function() (output replaces the function call; very end variable output will store whatever the output is)
```

**return** outputs the result. 

Think of them like a machine. Empty bottles. Function. Out comes a bottle of milk. Processes or code to create change.

## Print vs. Return

### Explanation of Current Code

At the moment we have these four functions below. When we call it, we pass over some inputs, and, when we get a hold of the output, we print it out in the console. 

What if we wanted to take the output that comes from calling this function and instead of just storing it inside a variable and then printing it out, what if we wanted to pass it as an input to another function?

What if we decided we wanted to ask them for another operation? We'll provide the previous answer in place in `num1` and `num3` in the palce of `num2`.

```py
# Add
def add(n1, n2):
  """Add two number to each other

  Args:
      n1 (int): Addend 1.
      n2 (int): Addend 2.

  Returns:
      int: The sum of the two addends.
  """
  return n1 + n2

# Subtract
def subtract(n1, n2):
  """Subtract two numbers from each other

  Args:
      n1 (int): The number (minuend) that will be subtracted from
      n2 (int): The amount (subtrahend) by which you subtract from another number

  Returns:
      int: The number (difference) that results from subtraction
  """
  return n1 - n2

# Multiply
def multiply(n1, n2):
  """Multiply two numbers

  Args:
      n1 (int): Factor 1. 
      n2 (int): Factor 2.

  Returns:
      int: The product of factor 1 and factor 2.
  """
  return n1 * n2

# Divide
def divide(n1, n2):
  """Divide two numbers

  Args:
      n1 (int): The number that is being divided (dividend)
      n2 (int): The number that is being divided by (divisor)

  Returns:
      int: The Quotient
  """
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

options = ""
for key in operations:
  options += key + ' '

# function = operations["*"]
# function(2, 3)

num1 = int(input("What's the first number?: "))
chosen_operation = input(f"{options}\nPick an operation from the line above: ")
num2 = int(input("What's the second number?: "))


# calculation_function = operations[chosen_operation]
# answer = calculation_function(num1, num2)

answer = operations[chosen_operation](num1, num2)

print(f"{num1} {chosen_operation} {num2} = {answer}")
```

### Demonstration of New Code

Because I have an output from my calc functions at the top, I'm able to take the result from the calculation and plug it right back into another calculation function using the result of that function call as an input to another function call.

I can only do this because I'm using the `return` statement and not the `print()` function.

```py
# Calculator

# Add
def add(n1, n2):
  """Add two number to each other

  Args:
  n1 (int): Addend 1.
  n2 (int): Addend 2.

  Returns:
  int: The sum of the two addends.
  """
  return n1 + n2

# Subtract
def subtract(n1, n2):
  """Subtract two numbers from each other

  Args:
  n1 (int): The number (minuend) that will be subtracted from
  n2 (int): The amount (subtrahend) by which you subtract from another number

  Returns:
  int: The number (difference) that results from subtraction
  """
  return n1 - n2

# Multiply
def multiply(n1, n2):
  """Multiply two numbers

  Args:
  n1 (int): Factor 1. 
  n2 (int): Factor 2.

  Returns:
  int: The product of factor 1 and factor 2.
  """
  return n1 * n2

# Divide
def divide(n1, n2):
  """Divide two numbers

  Args:
  n1 (int): The number that is being divided (dividend)
  n2 (int): The number that is being divided by (divisor)

  Returns:
  int: The Quotient
  """
  return n1 / n2

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide
}

options = ""
for key in operations:
  options += key + ' '

# function = operations["*"]
# function(2, 3)

num1 = int(input("What's the first number?: "))
chosen_operation = input(f"{options}\nPick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[chosen_operation]

# =========================== This is new ====================================
first_answer = calculation_function(num1, num2)

print(f"{num1} {chosen_operation} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[chosen_operation]
second_answer = calculation_function(first_answer, num3)


print(f"{first_answer} {chosen_operation} {num3} = {second_answer}")
# ==========^^=============== This is new ==========^^=======================

```

## Recursion

A function that calls itself.

Call the calculator function in order for it to find where the function was defined and carry out the instructions.

When the user types "no" that they don't want to calculating with the previous answer but instead want to start a new calculation, instead of just exiting the wild loop, we want to call the calculator function.

This will take us back to the beginning. 

Calling the calculator function within the calculator function.

Ought to be careful with while loops and recursions. Create a condition that needs to be met for this function to call itself.

```py
def calculator():
    options = ""
    for key in operations:
    options += key + ' '

    # function = operations["*"]
    # function(2, 3)


    num1 = int(input("What's the first number?: "))

    continue_calculating = True

    while continue_calculating:
        chosen_operation = input(f"{options}\nPick an operation from the line above operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[chosen_operation]
        answer = calculation_function(num1, num2)

        print(f"{num1} {chosen_operation} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
            num1 = answer
        else:
            continue_calculating = False
            calculator()
```