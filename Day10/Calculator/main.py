# Calculator
from art import logo

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

def calculator():
  print(logo)

  options = ""
  for key in operations:
    options += key + ' '

  # function = operations["*"]
  # function(2, 3)

  num1 = float(input("What's the first number?: "))

  continue_calculating = True

  while continue_calculating:
    chosen_operation = input(f"{options}\nPick an operation from the line above operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[chosen_operation]
    answer = calculation_function(num1, num2)

    print(f"{num1} {chosen_operation} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
      num1 = answer
    else:
      continue_calculating = False
      calculator()

calculator()







