# Day 26: List Comprehension and the NATO Alphabet

## How to Create Lists using List Comprehension

Unique to Python language. Other languages don't really have access to something like this. Makes code shorter and easier to read. 

*What is it?* It allows you to create a new list from a previous list.

### For Loop Example

```py
numbers = [1, 2, 3]

# create a new list where each number is increased by 1.
new_list = []
for n in numbers:
  add_1 = n+1
  new_list.append(add_1)
```

### List Comprehension
The above four lines of code can be turned into 1 with List Comprehension.
```py
new_list = [new_item for item in list]
```

The KEYWORD method, type out each of the list comprehension's keywords and then replace with the actual item in your code.

Create the name of the new list, open up a set of square brackets (creating a list), and do `new_item for item in list`. Using the lists from above, that would look like this:
- `new_list=[n+1   for n in numbers]`

List Comprehension doesn't only work with numbers. It works with *lists*, so can apply to strings and more.

#### Console Challenge
- **Create a new list from `numbers`, where you added 1 to each value**
```py
numbers = [1, 2, 3]
new_numbers = [number+1 for number in numbers]
```

#### Console Challenge
- **Predict what `new_list` will contain. Check your prediction in PyCharm.**

```py
name = "Angela"
new_list = [letter for letter in name]
```

**Prediction.** `new_list = ['A','n','g','e','l','a']`
**Answer.** `new_list = ['A','n','g','e','l','a']`

### Python Sequences
`list`
`range`
`string`
`tuple`

These are all called sequences because they have a specific order. When you perform a list comprehension, it's going to go through it in a specific order.

#### Challenge
- **Create a new list from a `range`, where the list items are double the values in the range.**

```py
range_values = range(1,11)
doubled_range_values = [number*2 for number in range_values]
print(doubled_range_values)
```

### Conditional List Comprehension

`new_list = [new_item for item in list if test]`

This takes our keywords a little bit further. We can also tag on two more keywords -- if and test.

```py
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
```

#### Challenge
- **Create a new list that contains the names longer than 5 characters in ALL CAPS**

```py
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 4]
```

---

## Squaring Numbers

```py
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number**2 for number in numbers]

#Write your code 👆 above:

print(squared_numbers)
```

---

## Filtering Even Numbers

### Instructions

You are going to write a List Comprehension to create a new list called `result`. This new list should only contain the even numbers from the list `numbers`.

DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

```py
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [number for number in numbers if number%2 == 0]

#Write your code 👆 above:

print(result)
```
---

## Data Overlap

### Instructions

Take a look inside **file1.txt** and **file2.txt**. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are **common** in both files.

e.g. if file1.txt contained
```
1
2
3
```

and file2.txt contained
```
2
3
4
```

result = [2, 3]

**IMPORTANT:** The result should be a list that contains **Integers**, not **Strings**. Try to use **List Comprehension** instead of a **Loop**.

```py
with open("file1.txt") as file1:
  numbers = file1.readlines()
  numbers_1 = [number.strip() for number in numbers]

with open("file2.txt") as file2:
  numbers = file2.readlines()
  numbers_2 = [number.strip() for number in numbers]

result = [int(number) for number in numbers_1 if number in numbers_2]

#Write your code 👆 above:

print(result)
```

---

## Apply List Comprehension to the U.S. States Game

```py
  if answer_state == "Exit":
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break
```

---

## How to use Dictionary Comprehension

**Dictionary Comprehension.** Allows us to create a new dictionary from the values in a list or a dictionary.

```py
new_dict = {new_key:new_value for item in list}
```

We could also create a new dictionary based on the values in an existing dictionary.
```py
new_dict = {new_key:new_value for (key,value) in dict.items()}
```

Conditional Dictionary Comprehension
```py
new_dict = {new_key:new_value for (key,value) in dict.items() if test}
```

### In Practice

Loop through a list to create a dictionary.
```py
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

"""THE GOAL: CREATE A DICTIONARY LIKE THIS
student_score = {
  "Alex": 89,
  "Beth": 98
}
"""

student_scores = {student:random.randint(1,100) for student in names}
```
Loop through a dictionary to create a dictionary.
```py
passed_students = {student:score for (student,score) in student_scores.items() if value > 60}
```

---

### Dictionary Comprehension 1

#### Instructions

You are going to use Dictionary Comprehension to create a dictionary called `result` that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

**Do NOT** Create a dictionary directly. Try to use **Dictionary Comprehension** instead of a **Loop**.

```py
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word:len(word) for word in sentence.split(" ")}


print(result)

```

---

### Dictionary Comprehension 2

#### Instructions

You are going to use Dictionary Comprehension to create a dictionary called `weather_f` that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert temp_c into temp_f:

(temp_c * 9/5) + 32 = temp_f

**Do NOT** Create a dictionary directly. Try to use **Dictionary Comprehension** instead of a **Loop**.

```py
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day:(degree * 9/5)+32 for (day,degree) in weather_c.items()}

print(weather_f)

```

---

## How to Iterate over a Pandas DataFrame

```py
student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 76, 98]
}
```

We can loop through a dictionary simply using a for loop.

```py
#Looping through dictionaries:
for (key, value) in student_dict.items():
  print(value)
```

Doing the same thing with List Comprehension on a DataFrame!

```py
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
```

```py
#Loop through a data frame
for (key, value) in student_data_frame.items():
  print(key) # gives me the name of the columns
  print(value) # gives me the values in the columns
```

The above isn't particularly useful. And **pandas** has an **inbuilt loop**.

The **index** correlates to the **row/record number**.
```py
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
  print(index)
  print(row.student) # each of these rows is a panda series object; we can tap into the row and get hold of the value using dot notation
  print(row.score) 
  if row.student == "Angela":
      print(row.score)
```

---

## Nato Project

```py
import pandas

#TODO 1. Create a dictionary in this format:
NATO_ALPHABET_PATH = r'C:\repos\100DaysOfPython\Day_26\nato_alphabet\nato_phonetic_alphabet.csv'
nato_alphabet = pandas.read_csv(NATO_ALPHABET_PATH)
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word to get its phonetic spelling: ").upper()

user_letters = [letter for letter in user_word]
# phonetic_code = [new_key:new_value for (key, value) in dict.items() if test]
phonetic_code = [nato_dict[letter] for letter in user_word]

print(phonetic_code)
```