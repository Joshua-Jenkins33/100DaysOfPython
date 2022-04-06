#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_pw = ''

for letter in range(0, nr_letters):
    index = random.randint(0,len(letters)-1)
    easy_pw += letters[index]

for symbol in range(0, nr_symbols):
    index = random.randint(0,len(symbols)-1)
    easy_pw += symbols[index]

for number in range(0, nr_numbers):
    index = random.randint(0,len(numbers)-1)
    easy_pw += numbers[index]

print(f'Your new password is: {easy_pw}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_pw = []
jumbled_pw = ''

for letter in range(0, nr_letters):
    index = random.randint(0,len(letters)-1)
    hard_pw.append(letters[index])

for symbol in range(0, nr_symbols):
    index = random.randint(0,len(symbols)-1)
    hard_pw.append(symbols[index])

for number in range(0, nr_numbers):
    index = random.randint(0,len(numbers)-1)
    hard_pw.append(numbers[index])

for character in hard_pw:
    randchar = random.randint(0,len(hard_pw)-1)
    jumbled_pw += hard_pw[randchar]

print(f'Your new password is: {jumbled_pw}')
