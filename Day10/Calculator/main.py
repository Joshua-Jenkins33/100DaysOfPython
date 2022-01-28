# Calculator
from art import logo
from functions import add, subtract, multiply, divide

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
}

def calculator():
  print(logo)

  options = ""
  for key in operations:
    options += key + ' '

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
      ## RECURSION
      calculator()

calculator()







