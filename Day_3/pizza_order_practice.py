# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
sp = 15
mp = 20
lp = 25
peps = 2
echeese = 1
total = 0

if size != 'S':
    if size == 'M':
        total += 20
    else:
        total += 25
    if add_pepperoni == 'Y':
        total += 3
else:
    total += 15
    if add_pepperoni == 'Y':
        total += 3
if extra_cheese == 'Y':
    total += 1

print(f'Your final bill is: ${int(total)}.')