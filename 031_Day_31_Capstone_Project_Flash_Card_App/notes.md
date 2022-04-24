# Day 31: Capstone Project — Flash Card App

## Step 1: Create the User Interface (UI) with Tkinter
1. Use the images in the image folder to create the user interface. 
2. Hints for the Fonts, measurements, and positioning.
    - Window 50px Padding
    - Language Label: x=400,y=150 | "Arial",40,"italic"
    - Word Label: x=400,y=263 | Font "Arial",60,"bold"
    - Card Width = 800px
    - Card Height = 526px
3. Additional Hints
    - 2x2 grid with flash card taking up 2 columns
    - Flash card is a [canvas](https://effbot.org/tkinterbook/canvas.htm) with 1 image and 2 pieces of text
    - The image is card_front.png created from the PhotoImage class. 

The ❌ and ✅ are buttons. You can add images to buttons like this:

```py
    my_image = PhotoImage(file="path/to/image_file.png")
    button = Button(image=my_image, highlightthickness=0)
```

**My Work.**
```py
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Text
language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", fill="black", font=("Arial", 60, "bold"))

# Buttons
image_insecurity = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\wrong.png")
insecurity_button = Button(image=image_insecurity, highlightthickness=0)
insecurity_button.grid(column=0,row=1)

image_confidence = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\right.png")
confident_button = Button(image=image_confidence, highlightthickness=0)
confident_button.grid(column=1,row=1)


window.mainloop()

```


## Solution & Walkthrough for Creating the UI

**Instructor Workthrough**
```py
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Text
language_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))

# Buttons
image_insecurity = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\wrong.png")
unknown_button = Button(image=image_insecurity, highlightthickness=0)
unknown_button.grid(row=1, column=0)

image_confidence = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\right.png")
check_button = Button(image=image_confidence, highlightthickness=0)
check_button.grid(row=1, column=1)


window.mainloop()
```

## Step 2: Create New Flash Cards
1. Read the data from the **french_words.csv** file in the **data** folder.
2. Pick a **random** French word/translation and put the word into the flashcard. Every time you press the :x: or :check: buttons, it should generate a **new random word** to display.

***Hints***
1. You'll need to use pandas to access the CSV file and generate a data frame. To get all the words/translations rows out as a list of dictionaries.

You could use `DataFrame.to_dict(orient="records")`

[Documentation -- Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html)

```py
# ---------------------------- CREATE FLASH CARDS ------------------------------- #


french_df = pandas.read_csv(FRENCH_WORDS_PATH)
french_list_dict = french_df.to_dict(orient="records")

def get_random_word():
    new_word = random.choice(french_list_dict)['French']
    canvas.itemconfig(word_text, text=f"{new_word}")
    print(new_word['French'])

insecurity_button = Button(image=image_insecurity, highlightthickness=0, command=get_random_word)
confident_button = Button(image=image_confidence, highlightthickness=0,command=get_random_word)
```

## Solution & Walkthrough for Creating New Flash Cards

Same as my code above except the function was called `def next_card():`.

```py
french_df = pandas.read_csv(FRENCH_WORDS_PATH)
french_list_dict = french_df.to_dict(orient="records")

def get_random_word():
    new_word = random.choice(french_list_dict)
    canvas.itemconfig(word_text, text=f"{new_word}['French']")
    canvas.itemconfig(language_text, text=f"French")
```

## Step 3: Flip the Cards!
1. After a 3 second delay, the card should flip and display the **English Translation** for the current word.
2. The card image should change to the **card_back.png** and the text coulur should change to **white**. The **title** of the card should change to *English* from *French.*

**Hints**
1. To change the canvas image, you'll need a reference to the image, like what you have with the text created in the canvas. Then you can set the image attribute using `itemconfig()`.

```py
new_image = PhotoImage(file="new_image.png")
old_image = PhotoImage(file="old_image.png")
canvas_image = canvas.create_image(300, 300, image=old_image)
# To change the image
canvas.itemconfig(canvas_image, image=new_image)
```

IMPORTANT: PhotoImage objects should not be created inside a function. Otherwise, it will not work.

2. Change the color of the text in a canvas element, use the `fill` parameter. e.g. [How can I change the color of text in tkinter]()

3. Remember in the `mainloop()` you should **not** create additional delayed loops e.g. with `time.sleep()` but instead, use `window.after()` [Tkinter Reference Manual: .after method]()

4. You can cancel a `window.after()` loop using `window.after_cancel()` [Tkinter Reference Manual: .after_cancel() method]()

## Solution & Walkthrough for Flipping Cards

```py
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_WORDS_PATH = r'031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\data\french_words.csv'
IMG_CARD_FRONT = r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\card_front.png"
CARD_BACK = r'G:\Main\Development\100DaysOfPython\031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\card_back.png'

# ---------------------------- CREATE FLASH CARDS ------------------------------- #


french_df = pandas.read_csv(FRENCH_WORDS_PATH)
to_learn = french_df.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(card_word, text=f"French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back)
    english_translation_word = current_card['English']
    
    
    canvas.itemconfig(card_title, text=f"{english_translation_word}", fill="white")
    canvas.itemconfig(card_word, text=f"English", fill="white")
    

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
card_word = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_title = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

# Buttons
image_insecurity = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\wrong.png")
insecurity_button = Button(image=image_insecurity, highlightthickness=0, command=next_card)
insecurity_button.grid(column=0,row=1)

image_confidence = PhotoImage(file=r"031_Day_31_Capstone_Project_Flash_Card_App\Flash_Card_App\images\right.png")
confident_button = Button(image=image_confidence, highlightthickness=0,command=next_card)
confident_button.grid(column=1,row=1)


window.mainloop()

```

## Step 4: Save Your Progress
1. When the user presses on the :check: button, it means that they know the current word on the flashcard and that word should be removed from the list of words that might come up.

e.g. if `french_words.csv` had only 3 records:
> chaque,each
> parlé,speak
> arrivé,come

After the user has seen `parlé,speak` it should be **removed** from the list of words that can come up again.

2. The updated data should be saved to a new file called **words_to_learn.csv**

e.g. `words_to_learn.csv`
> chaque,each
> arrivé,come

3. The next time the program is run, it should check if there is a `words_to_learn.csv` file. If it exists, the program should use those words to put on the flashcards. If the `words_to_learn.csv` does not exist (i.e., the first time the program is run), then it should use the words in the `french_words.csv`

We want our flashcard program to only test us on things we don't know. So if the user presses the ✅ button, that means the current card should not come up again.

**HINTS:**
1. The `remove()` [method can remove elements from a list](https://www.w3schools.com/python/ref_list_remove.asp). 
2. You can [create a new csv file from a dictionary](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) using `DataFrame.to_csv()`.
3. If you don't want to create an index for the new csv, you can set the index parameter to False. e.g.
> `data.to_csv("filename.csv", index=False) `

## Solution & Walkthrough for Saving Progress
The goal in this section is to remove words from the `to_learn` list that the user doesn't want to see anymore—because they've mastered that word.

This shows how to remove words from the list. But it resets upon application restart. We need to save the reduced list to a new, permanent file.
```py
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()
```
We need to save the reduced list to a new, permanent file.
```py
# def is_known():
#     to_learn.remove(current_card)
#     print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv")

#     next_card()
```

Now I need to read from the new file. We do need to catch an exception, though, if the file doesn't exist.

```py
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

```

Pandas is adding in record numbers. To remove those, set a property called `index` to false.
```py
# def is_known():
#     to_learn.remove(current_card)
#     print(len(to_learn))
    # data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)

#     next_card()
```

And the final result:
```py
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
```