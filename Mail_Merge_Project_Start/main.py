#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Mail_Merge_Project_Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
file = open("Mail_Merge_Project_Start/Input/Letters/starting_letter.txt")
x = file.read()
for name in names:
    stripped_name = name.strip()
    y = x.replace("[name]", stripped_name) 
    with open(f"Mail_Merge_Project_Start/Output/ReadyToSend/{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(y)