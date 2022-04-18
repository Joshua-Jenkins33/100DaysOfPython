# Day 29: Tkinter -- Building a Password Manage GUI App

## Challenge 1: Working with Images and Setting up the Canvas

We are going to create a window with a title of "Password Manager", and it will have a canvas widget displaying the logo image. The canvas is 200x200 and padded from the edge of the window by 20 pixels from all four sides. The image needs to be in the center of the canvas.

```py
from tkinter import Tk, Canvas, PhotoImage

# ---------------------------- UI SETUP ------------------------------- #

LOGO = r'G:\Main\Development\100DaysOfPython\Day_29_Tkinter_PasswordManager\Password_Manager\media\logo.png'
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=LOGO)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0)

window.mainloop()
```

## Challenge 2: Use `grid()` and `columnspan` to Complete the User Interface

We are going to need to add widgets and have a bit more complicated knowledge about how to add widgets in a complex layout.

### Grid Columnspan Demo

This is used as an example to demonstrate/visualize how the grid system works and how you can make more complicated layouts.

```py
from tkinter import *
window = Tk()

r = Lbale(bg="red", width=20, height =5)
r.grid(row=0, column=0)

g = Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

b = Label(bg="blue", width=40, height=5)
b.grid(row=2, column=0, columnspan=2)

window.mainloop()
```

### Challenge Details

Three column and five row layout.

#### Labels
1. Website
- column=0, row=1
2. Email/Username
- column=0, row=2
3. Password
- column=0, row=3

#### Text Fields
1. Website (Width: 35)
- column=1, row=1
2. Email/Username
- column=1, row=2
3. Password (Width: 21)
- column=1, row=3

#### Buttons
1. Generate Password
- column=2, row=3
2. Add (Width: 36)
- column=1, row=4, columnspan=2

```py
# ---------------------------- UI SETUP ------------------------------- #

# LOGO = r'G:\Main\Development\100DaysOfPython\Day_29_Tkinter_PasswordManager\Password_Manager\media\logo.png'
# window = Tk()
# window.title("Password Manager")
# window.config(padx=20, pady=20)

# canvas = Canvas(width=200, height=200)
# logo_img = PhotoImage(file=LOGO)
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(column=0, row=0)

label_website = Label(text="Website: ")
label_website.grid(column=0, row=1)

label_email_or_username = Label(text="Email/Username: ")
label_email_or_username.grid(column=0, row=2)

label_password = Label(text="Password: ")
label_password.grid(column=0, row=3)

button_generate_password = Button(text="Generate Password")
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=34)
button_add.grid(column=1, row=4, columnspan=2)

entry_website = Entry(text="", width=41)
entry_website.grid(column=1, row=1, columnspan=2)

entry_email_or_username = Entry(text="", width=41)
entry_email_or_username.grid(column=1, row=2, columnspan=2)

entry_password = Entry(text="", width=21)
entry_password.grid(column=1, row=3)

# window.mainloop()
```

## Challenge 3: Saving Data to File
Get the cursor in the first file!

```py
entry_website.focus()
```

Insert our email address automagically!

```py
entry_email_or_username.insert(0, "test@test.com")
```

Take the inputs from the website, email, and password entry, save that data into a file called data.text. Have them separated by a `space | space`.

### Tasks

1. Create a function called `save()`.
2. Write to the data inside the entries to a `data.txt` file when the `Add button` is clicked.
3. Each website, email, and password combination should be on a new line inside the file.
4. All fields need to be cleared after `Add button` is pressed.

```py
# ---------------------------- SAVE PASSWORD ------------------------------- #

def remove_entries():
    entry_website.delete(0,'end')
    #entry_email_or_username.delete(0,'end')
    entry_password.delete(0,'end')


def save():
    with open("data.txt", "a") as file:
        file.write(f"{entry_website.get()} | {entry_email_or_username.get()} | {entry_password.get()}\n")
    
    remove_entries()


button_add = Button(text="Add", width=34, command=save)

entry_password = Entry(text="", width=21, textvariable='password', show="*")
entry_password.grid(column=1, row=3)

```

## Dialog Boxes and Pop-Ups in Tkinter
Now we need to create a confirmation of knowing whether or not your command was successful and to verify the data looks how the user expected.

The answer? **Standard Dialogs.** **Message Boxes** are some of the most popular.

You have to import messagebox separately; `from tkinter import *` only grabs classes; messagebox is its own module within Tkinter.

```py
# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
# def remove_entries():
#     entry_website.delete(0,'end')
#     #entry_email_or_username.delete(0,'end')
#     entry_password.delete(0,'end')

    


def save():
    website = entry_website.get()
    email = entry_email_or_username.get()
    password = entry_password.get()

    messagebox.showinfo(title="Title", message="Message")
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?")

    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{entry_website.get()} | {entry_email_or_username.get()} | {entry_password.get()}\n")
        
        remove_entries()


# button_add = Button(text="Add", width=34, command=save)

# entry_password = Entry(text="", width=21, textvariable='password', show="*")
# entry_password.grid(column=1, row=3)
```

### Challenge: Data Validation

Do not save the data and show the pop up above if the website or password fields were left empty.

```py
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
        is_ok = messagebox.askokcancel(title=fields_list[0]['website'], message=f"These are the details entered: \n\nEmail: {fields_list[1]['email']}\nPassword: {fields_list[2]['password']} \n\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{fields_list[0]['website']} | {fields_list[1]['email']} | {fields_list[2]['password']}\n")
            
            remove_entries()
```

## Generate a Password & Copy it to the Clipboard

We are reusing modified code from [Day 5](https://github.com/Joshua-Jenkins33/100DaysOfPython/blob/main/Day_5_Python_Loops/Day5.md) for our Password Generator code.

### Challenge: Change the Code to Use List Comprehension

- Change the existing `for loops` to use Python List Comprehension instead (see [Day 26](https://github.com/Joshua-Jenkins33/100DaysOfPython/blob/main/Day_26_List_Comprehension_Nato/notes.md)).
- Remember to combine the results so that you can shuffle them to create a password.

```py
password_letters = [choice(letters) for _ in range(randint(8, 10))]
password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

password_list = password_letters + password_symbols + password_numbers

shuffle(password_list)

password = "".join(password_list)

print(f"Your password is: {password}")
```

### Challenge: Populate the Field with the Generated Password

```py
def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

#     password_list = password_letters + password_symbols + password_numbers

#     shuffle(password_list)

#     password = "".join(password_list)


    entry_password.delete(0,'end')
    entry_password.insert(0,password)
```

### Use `pyperclip` to automagically stick the password in your clipboard

The link to the module is [here](https://pypi.org/project/pyperclip/).

```py
# install the pyperclip module with pip install pyperclip (make sure you're in the right venv!)

# import the module
import pyperclip

# call the module .copy method

def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

#     password_list = password_letters + password_symbols + password_numbers

#     shuffle(password_list)

#     password = "".join(password_list)


#     entry_password.delete(0,'end')
#     entry_password.insert(0,password)
    pyperclip.copy(password)
```