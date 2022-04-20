import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
  word = input("Enter a word: ").upper()
  #TODO: what happens if the user adds something that isn't a letter?
  #TODO: how do we loop the code?
  try:
    output_list = [phonetic_dict[letter] for letter in word]
  except ValueError:
    print("Sorry, that's not valid letter.")
    generate_phonetic()
  else:
    print(output_list)

generate_phonetic()