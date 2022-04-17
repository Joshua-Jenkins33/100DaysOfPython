from tkinter import Tk, Canvas, PhotoImage, Label, Button, Entry

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def remove_entries():
    entry_website.delete(0,'end')
    #entry_email_or_username.delete(0,'end')
    entry_password.delete(0,'end')


def save():
    with open("data.txt", "a") as file:
        file.write(f"{entry_website.get()} | {entry_email_or_username.get()} | {entry_password.get()}\n")
    
    remove_entries()


# ---------------------------- UI SETUP ------------------------------- #

LOGO = r'G:\Main\Development\100DaysOfPython\Day_29_Tkinter_PasswordManager\Password_Manager\media\logo.png'
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=LOGO)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0)

label_website = Label(text="Website: ")
label_website.grid(column=0, row=1)

label_email_or_username = Label(text="Email/Username: ")
label_email_or_username.grid(column=0, row=2)

label_password = Label(text="Password: ")
label_password.grid(column=0, row=3)

button_generate_password = Button(text="Generate Password")
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=34, command=save)
button_add.grid(column=1, row=4, columnspan=2)

entry_website = Entry(text="", width=41)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_email_or_username = Entry(text="", width=41)
entry_email_or_username.grid(column=1, row=2, columnspan=2)
entry_email_or_username.insert(0, "test@test.com")

entry_password = Entry(text="", width=21, textvariable='password', show="*")
entry_password.grid(column=1, row=3)

window.mainloop()