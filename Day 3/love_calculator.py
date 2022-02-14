# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


test1 = 'TRUE'.lower()
test2 = 'LOVE'.lower()
name1 = name1.lower()
name2 = name2.lower()
true_score = 0
love_score = 0

for letter in test1:
    for name_letter in name1:
        if name_letter == letter:
            true_score += 1
    for name_letter in name2:
        if name_letter == letter:
            true_score += 1
for letter in test2:
    for name_letter in name1:
        if name_letter == letter:
            love_score += 1
    for name_letter in name2:
        if name_letter == letter:
            love_score += 1

score = str(true_score) + str(love_score)

if int(score) < 10 or int(score) > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif int(score) <= 50 and int(score) >= 40:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')