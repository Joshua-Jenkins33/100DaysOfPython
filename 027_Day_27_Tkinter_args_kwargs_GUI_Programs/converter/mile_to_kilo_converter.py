from tkinter import *

def convert_miles_to_kilometers():
  miles = int(entry.get())
  miles *= 1.609344
  the_conversion_label_value.config(text=str(miles))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=30, pady=30)

entry = Entry(text="0")
entry.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0,row=1)

the_conversion_label_value = Label(text="0")
the_conversion_label_value.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert_miles_to_kilometers)
calculate_button.grid(column=1, row=2)

window.mainloop()


