# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
check = number%2
result = 0
if check < 1:
    result = "This is an even number."
else:
    result = "This is an odd number."

print(result)
