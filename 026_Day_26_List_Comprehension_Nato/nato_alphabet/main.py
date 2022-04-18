student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
NATO_ALPHABET_PATH = r'C:\repos\100DaysOfPython\Day_26\nato_alphabet\nato_phonetic_alphabet.csv'
nato_alphabet = pandas.read_csv(NATO_ALPHABET_PATH)
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word to get its phonetic spelling: ").upper()

user_letters = [letter for letter in user_word]
# phonetic_code = [new_key:new_value for (key, value) in dict.items() if test]
phonetic_code = [nato_dict[letter] for letter in user_word]

print(phonetic_code)
