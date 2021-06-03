
import datetime as dt
import random
import smtplib
my_email = "ex100code@gmail..com"
password = "Nurdan90."

with open("Birthday_Wisher/quotes.txt", "r", encoding="utf-8") as message:
    monday_message = message.readlines()
    day_message = random.choice(monday_message)

def send_message():
    mail = smtplib.SMTP("smtp.gmail.com")
    mail.starttls()
    mail.login(user=my_email, password=password)
    mail.sendmail(from_addr=my_email, to_addrs="ex100code@yahoo.com", msg=day_message)




now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    print(day_message)
    send_message()











#import smtplib
#
#my_email = "ex100code@yahoo.com"
#password = "kqyelometxmrnmax"
#
#with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email, to_addrs="ex100code@gmail.com", msg="Hello")



#import datetime as dt
#
#
#
#now = dt.datetime.now()
#year = now.year
#month = now.month
#day_of_week = now.weekday()
#print(day_of_week)
#
#date_of_birth = dt.datetime(year=1986, month=8, day=31, hour=2)
#print(date_of_birth)