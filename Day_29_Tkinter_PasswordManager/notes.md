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

```

## Dialog Boxes and Pop-Ups in Tkinter

## Generate a Password & Copy it to the Clipboard