# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_in_days = 90*365
total_in_weeks = 90*52
total_in_months = 90*12

time_lived_in_days = int(age)*365
time_lived_in_weeks = int(age)*52
time_lived_in_months = int(age)*12

x = total_in_days - time_lived_in_days
y = total_in_weeks - time_lived_in_weeks
z = total_in_months - time_lived_in_months

print(f'You have {x} days, {y} weeks, and {z} months left.')


# years = 90 - int(age)
# months = round(years * 12)
# weeks = round(years * 52)
# days = round(years * 365)

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")
