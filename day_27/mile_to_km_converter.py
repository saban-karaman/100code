
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)
# window.minsize(width=300, height=100)

def action():
    x = float(entry.get())
    y = x * 1.609
    label_3.config(text=str(y))
button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)

label_3 = Label(text="0")
label_3.grid(row=1, column=1)

label_4 = Label(text="Km")
label_4.grid(row=1, column=2)









window.mainloop()