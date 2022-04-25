from tkinter import *
import requests

'''
1. Make a `get()` request to the Kanye Rest API
2. Raise an exception if the request returned an unsuccessful **status code**.
3. Parse the `JSON` to obtain the quote text.
4. Display the quote in the canvas' `quote_text` widget.
'''


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=f"{data['quote']}")
    




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"033_Day_33_API_Endpoints_and_API_Parameters_ISS_Overhead_Notifier\kanye_quotes\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"033_Day_33_API_Endpoints_and_API_Parameters_ISS_Overhead_Notifier\kanye_quotes\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()