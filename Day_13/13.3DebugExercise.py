for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: # change *or* operator to *and* operator
    print("FizzBuzz")
  elif number % 3 == 0: # put this into an elif
    print("Fizz")
  elif number % 5 == 0: # put this into an elif
    print("Buzz")
  else:
    print(number) # don't print a list; that's silly