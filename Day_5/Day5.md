# Day 5

## Using the loop with Python Lists

```py
fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
```

## For Loops and the range() function

```py
for number in range(a, b):
    print(number)
```

Creating a range between A and B!

```py
for number in range(1, 10): # between 1 and 10, not including 10
    print(number)

for number in range(1, 11, 3):
    print(number)
```

By default, the range function will step through all numbers from start to end and increase by 1. If you want it to increase by any other number, add a comma and a new number for the step size.

```py
total = 0

for number in range(1, 101):
    total += number
print(total)
```

## 5.3 Adding Evens Options

### Range Parameters
```py
total = 0
for number in range(2, 101, 2):
    total += number    
print(number)
```

### Using % Modulus
```py
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(total)
```

## 5.4 FizzBuzz Options

### The Right Way!

```py
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```

## 5.5 Password Generator

### Easy Level

```py
password = ''
#nr_letters = 4
for char in range(1, nr_letters + 1):
    ##1 - 4
    #random_char = random.choice(letters)
    #print(random_char)
    #password += random_char
    #print(password)
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(symbols)
```

### Hard Level

```py
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''
for character in password_list:
    password += character

print(f'Your password is: {password}')
```