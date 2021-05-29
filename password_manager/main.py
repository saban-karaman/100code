from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    entry_pass.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web = entry_web.get()
    mail = entry_mail.get()
    pass_ = entry_pass.get()

    if web=="" or mail=="" or pass_ == "":
        is_empty = messagebox.askretrycancel(title="Ooops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {mail}"
                                              f"\nPassword: {pass_} \nIs it ok to save?")
    
    
    if is_ok:

        with open("password_manager/data.txt", "a", encoding="utf-8") as d:
            d.write(f"{web} | {mail} | {pass_}\n")
        entry_pass.delete(0, END)
        entry_mail.delete(0, END)
        entry_web.delete(0, END)

    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=220, height=220)
pass_img = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)
#canvas.pack()



#Labels
label_web = Label(text="Website:")
label_web.grid(row=1, column=0)

label_email = Label(text="Email/Username")
label_email.grid(row=2, column=0)

label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

#Buttons
button_pass = Button(text="Generate Password", command=generate)
button_pass.grid(row=3, column=2)

button_add = Button(text="Add", width=30, command=add)
button_add.grid(row=4, column=1, columnspan=2)

#Entries

entry_web = Entry(width=35)
entry_web.grid(row=1, column=1, columnspan=2)
entry_web.focus()
 

entry_mail = Entry(width=35)
entry_mail.grid(row=2, column=1, columnspan=2)



entry_pass = Entry(width=17)
entry_pass.grid(row=3, column=1)









window.mainloop()