student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

nato_alp = pandas.read_csv("NATO_alphabet-_start/nato_phonetic_alphabet.csv")
#for (index, row) in nato_alp.iterrows():
 #   print(row.letter, row.code)
nato_alpa = {row.letter: row.code for (index, row) in nato_alp.iterrows()}

x = input("give a word for change NATO code :").upper()
result = [nato_alpa[i] for i in x if i in nato_alpa.keys()]
print(result)