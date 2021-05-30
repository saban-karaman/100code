#student_dict = {
#    "student": ["Angela", "James", "Lily"], 
#    "score": [56, 76, 98]
#}
#
##Looping through dictionaries:
#for (key, value) in student_dict.items():
#    #Access key and value
#    pass
#
#import pandas
#student_data_frame = pandas.DataFrame(student_dict)
#
##Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
#    #Access index and row
#    #Access row.student or row.score
#    pass
#
## Keyword Method with iterrows()
## {new_key:new_value for (index, row) in df.iterrows()}
#
##TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
#
##TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
#nato_alp = pandas.read_csv("NATO_alphabet-_start/nato_phonetic_alphabet.csv")
##for (index, row) in nato_alp.iterrows():
# #   print(row.letter, row.code)
#
#
#
#
#nato_alpa = {row.letter: row.code for (index, row) in nato_alp.iterrows()}
#
#def generate():
#    x = input("give a word for change NATO code :").upper()
#    try:
#        result = [nato_alpa[i] for i in x]
#    except :
#        print("Sorry, only letters in the alphabet please")
#        generate()
#    else:
#        print(result)
#generate()



from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json




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
    new_data = {
        web: {
            "email":mail,
            "password":pass_,
            }
    }

    if web=="" or mail=="" or pass_ == "":
        is_empty = messagebox.askretrycancel(title="Ooops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("day_30/data.json", "r", encoding="utf-8") as d:
                #Reading old data
                data = json.load(d)
                #Updating old data with new data
                data.update(new_data)
            
        except FileNotFoundError:
            with open("day_30/data.json", "w", encoding="utf-8") as d:
                json.dump(new_data, d, indent=4)
        else:
            with open("day_30/data.json", "w", encoding="utf-8") as d:
                #Saving updated data
                json.dump(data, d, indent=4)
        finally:
            entry_pass.delete(0, END)
            entry_mail.delete(0, END)
            entry_web.delete(0, END) 

def search():
    web = entry_web.get()
    with open("day_30/data.json", "r", encoding="utf-8") as d:
            data = json.load(d)
    
            try:
                messagebox.showinfo(title=web, message=f"Email: {data[web]['email']}\nPassword: {data[web]['password']} ")
            except:
                messagebox.showinfo(title="Error", message="No Data File Found")
            
    

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

button_search = Button(text="Search", width=14, command=search)
button_search.grid(row=1, column=2)

#Entries

entry_web = Entry(width=17)
entry_web.grid(row=1, column=1)
entry_web.focus()
 

entry_mail = Entry(width=35)
entry_mail.grid(row=2, column=1, columnspan=2)



entry_pass = Entry(width=17)
entry_pass.grid(row=3, column=1)









window.mainloop()