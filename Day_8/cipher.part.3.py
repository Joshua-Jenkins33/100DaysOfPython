alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(command,input_text,shift_amount):
    reverted_text = ''    
    text_type = []
    
    for letter in input_text:
        position = alphabet.index(letter)
        if command == 'encode':
            new_position = position + shift_amount
            text_type = ['decoded','encoded']
        else:
            new_position = position - shift_amount
            text_type = ['encoded','decoded']
        reverted_text += alphabet[new_position]
    
    print(f'The {text_type[0]} text has been {text_type[1]} to {reverted_text}.')

'''
INSTRUCTOR CODE
def caesar(start_text, shift_amount, cipher_direction):
    end_test = ''
    if cipher_direction == 'decode':
    shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f'The {cipher_direction}d text is {end_text}')

caesar(start_text=text, shift_amount=shift,cipher_direction=direction)
'''


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(command=direction, input_text=text, shift_amount=shift)