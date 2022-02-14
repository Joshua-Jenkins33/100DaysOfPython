# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
verdict = ''
if year%4 == 0:
    verdict = 'Leap year.'
    if year%100 == 0:
        verdict = 'Not leap year.'
        if year%400 == 0:
            verdict = 'Leap year.'
else:
    verdict = 'Not leap year.'

print(verdict)



