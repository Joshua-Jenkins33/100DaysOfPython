# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
current_high = 0

for score in student_scores:
    if score > current_high:
        current_high = score

highest_score = current_high

result = f'The highest score in the class is: {highest_score}'
print(result)

'''
print(max(student_scores))
print(min(student_scores))
'''