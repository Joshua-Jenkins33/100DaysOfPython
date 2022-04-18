from tkinter import Tk, Canvas, PhotoImage, Label, Button, Entry, messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    #print(f"Your password is: {password}")
    entry_password.delete(0,'end')
    entry_password.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def remove_entries():
    entry_website.delete(0,'end')
    #entry_email_or_username.delete(0,'end')
    entry_password.delete(0,'end')


def format_error_message(error_list):
    ', '.join(error_list)
    error_message = f"Looks like you're missing a value for the following fields: {error_list}\n\nPlease populate these and try again."
    return error_message


def validate_fields_for_populated_values(fields_list: list):
    validation_results = {"fail": False, "failed_fields": []}
    for field in fields_list:
        if len(field['field_value']) == 0:
            validation_results["fail"] = True
            validation_results["failed_fields"].append(field['field_name'])
    return validation_results


def save():
    fields_list = [
        {
            "field_name": "website",
            "field_value": entry_website.get()
        },
        {
            "field_name": "email",
            "field_value": entry_email_or_username.get()
        },
        {
            "field_name": "password",
            "field_value": entry_password.get()
        },
    ]

    validation_results = validate_fields_for_populated_values(fields_list)
    if validation_results["fail"] == True:
        messagebox.showerror(title="Oops!", message=format_error_message(validation_results['failed_fields']))

    else:
        is_ok = messagebox.askokcancel(title=fields_list[0]['field_value'], message=f"These are the details entered: \n\nEmail: {fields_list[1]['field_value']}\nPassword: {fields_list[2]['field_value']} \n\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{fields_list[0]['field_value']} | {fields_list[1]['field_value']} | {fields_list[2]['field_value']}\n")
            
            remove_entries()


# ---------------------------- UI SETUP ------------------------------- #

LOGO = r'G:\Main\Development\100DaysOfPython\Day_29_Tkinter_PasswordManager\Password_Manager\media\logo.png'
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=LOGO)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email_or_username = Label(text="Email/Username:")
label_email_or_username.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=34, command=save)
button_add.grid(column=1, row=4, columnspan=2)

entry_website = Entry(text="", width=41)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_email_or_username = Entry(text="", width=41)
entry_email_or_username.grid(column=1, row=2, columnspan=2)
entry_email_or_username.insert(0, "test@test.com")

# entry_password = Entry(text="", width=23, textvariable='password', show="*")
entry_password = Entry(text="", width=23)
entry_password.grid(column=1, row=3)

window.mainloop()