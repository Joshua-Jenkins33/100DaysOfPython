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

## Step 4: Save Your Progress

## Solution & Walkthrough for Saving Progress