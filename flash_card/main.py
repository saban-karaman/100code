from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="flash_card/images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=front_img)

back_img = PhotoImage("flash_card/images/card_back.png")



card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


french = pandas.read_csv("flash_card/data/french_words.csv")
french_dict = {row.French: row.English for (index, row) in french.iterrows()}
words = ""

def screen_eng():
    global words
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=french_dict[words], fill="White")  
    canvas.itemconfig(canvas_img, image=back_img)
    
def screen_fr():
    global words, flip_timer
    window.after_cancel(flip_timer)
    word = [i for i in french_dict.keys()]
    canvas.itemconfig(card_title, text="French", fill="Black")
    words = random.choice(word)
    canvas.itemconfig(card_word, text=words, fill="Black")  
    canvas.itemconfig(canvas_img, image=front_img)
    flip_timer = window.after(ms=3000, func=screen_eng)

    
    
flip_timer = window.after(ms=3000, func=screen_eng)

#buttons
button_right_img = PhotoImage(file="flash_card/images/right.png")
button_right = Button(image=button_right_img, highlightthickness=0, width=50, height=50, command=screen_fr)
button_right.grid(row=1, column=0)

button_wrong_img = PhotoImage(file="flash_card/images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0, width=50, height=50, command=screen_fr)
button_wrong.grid(row=1, column=1)


screen_fr()








window.mainloop()












