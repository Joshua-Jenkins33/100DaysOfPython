#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

TEMPLATE_FILE_PATH = r'C:\repos\100DaysOfPython\Day_24\my_code\mail_merging\Input\Letters\starting_letter.txt'
NAMES_FILE_PATH = r'C:\repos\100DaysOfPython\Day_24\my_code\mail_merging\Input\Names\invited_names.txt'
READY_TO_SEND_PATH = r'C:\repos\100DaysOfPython\Day_24\my_code\mail_merging\Output\ReadyToSend'

with open(NAMES_FILE_PATH) as names_file:
    for name in names_file.readlines():
        letter_text = ''
        with open(TEMPLATE_FILE_PATH) as template_file:
            letter_text = template_file.readlines()
            greeting_line = letter_text[0].replace('[name]', name.strip())
            letter_text[0] = greeting_line
            with open(READY_TO_SEND_PATH+f'\{name.strip()}_invite.txt', 'w') as write_file:
                for line in letter_text:
                    write_file.write(line)

            
