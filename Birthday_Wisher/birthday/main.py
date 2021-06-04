##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas
import datetime as dt

data = [
    ["ivan", "aiv@gmail.com", "1983", "15", "7"]
    ]

dataframe = pandas.DataFrame(data)
dataframe.to_csv("Birthday_Wisher/birthday/birthdays.csv", index=False, mode="a", header=False)

now = dt.datetime.now()
day = now.day
month = now.month

with open("Birthday_Wisher/birthday/birthdays.csv", "r", encoding="utf-8") as f:
    birtdays = f.readlines()



full_data = pandas.read_csv("Birthday_Wisher/birthday/birthdays.csv")
first= full_data[["month", "day"]]
print(first.iloc[month])

