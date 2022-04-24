from tkinter import *
import pandas
import random
from os.path import exists

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_WORDS_PATH = r'031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\data\french_words.csv'
IMG_CARD_FRONT = r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\card_front.png"
CARD_BACK = r'G:\Main\Development\100DaysOfPython\031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\card_back.png'

# ---------------------------- MANAGE TO-LEARN LIST ------------------------------- #
def determine_learning_data_set():
    if exists(r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\data\words_to_learn.csv"):
        print("Using modified data set.")
        return pandas.read_csv(r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\data\words_to_learn.csv")
    else:
        print("Using total data set.")
        return pandas.read_csv(FRENCH_WORDS_PATH)


# ---------------------------- CREATE FLASH CARDS ------------------------------- #


french_df = determine_learning_data_set()
to_learn = french_df.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def remove_word():
    global current_card

    if len(current_card) != 0:
        to_learn.remove(current_card)
        if current_card not in to_learn:
            print(f"Congratulations! You've learned the word: {current_card['French']}! It has been removed from your learning list.")
    update_WIP_data_set()

def update_WIP_data_set():
    updated_to_learn = pandas.DataFrame(to_learn)
    updated_to_learn.to_csv(r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\data\words_to_learn.csv", index=False)
    next_card()


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file=CARD_BACK)
card_front = PhotoImage(file=IMG_CARD_FRONT)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Text
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

# Buttons
image_insecurity = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\wrong.png")
insecurity_button = Button(image=image_insecurity, highlightthickness=0, command=next_card)
insecurity_button.grid(column=0,row=1)

image_confidence = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\right.png")
confident_button = Button(image=image_confidence, highlightthickness=0,command=remove_word)
confident_button.grid(column=1,row=1)

next_card()

window.mainloop()
