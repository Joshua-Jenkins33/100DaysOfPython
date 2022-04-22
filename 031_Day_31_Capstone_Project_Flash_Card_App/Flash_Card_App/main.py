from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_WORDS_PATH = r'031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\data\french_words.csv'


# ---------------------------- CREATE FLASH CARDS ------------------------------- #


french_df = pandas.read_csv(FRENCH_WORDS_PATH)
french_list_dict = french_df.to_dict(orient="records")

def get_random_word():
    new_word = random.choice(french_list_dict)
    canvas.itemconfig(word_text, text=f"{new_word['French']}")
    canvas.itemconfig(language_text, text=f"French")
    print(new_word['French'])

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Text
language_text = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

# Buttons
image_insecurity = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\wrong.png")
insecurity_button = Button(image=image_insecurity, highlightthickness=0, command=get_random_word)
insecurity_button.grid(column=0,row=1)

image_confidence = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\right.png")
confident_button = Button(image=image_confidence, highlightthickness=0,command=get_random_word)
confident_button.grid(column=1,row=1)


window.mainloop()
