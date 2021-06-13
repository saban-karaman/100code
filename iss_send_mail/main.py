from tkinter.constants import TRUE
import requests
from datetime import datetime
import smtplib
import time

my_email= "ex100code@gmail.com"
password = "Ankara06."

def send_message():
    mail = smtplib.SMTP("smtp.gmail.com")
    mail.starttls()
    mail.login(user=my_email, password=password)
    mail.sendmail(from_addr=my_email, to_addrs="ex100code@yahoo.com", msg="ISS is now your sky") 

MY_LAT = 41.008240
MY_LNG = 28.978359

def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data_iss = response_iss.json()

    iss_longitude = float(data_iss["iss_position"]["longitude"])
    iss_latitude = float(data_iss["iss_position"]["latitude"])

    iss_position = (iss_latitude, iss_longitude)
    # print(iss_position)
    if (MY_LAT >= iss_latitude-5 and MY_LAT <= iss_latitude+5) and (MY_LNG >= iss_latitude-5 and MY_LNG <= iss_latitude+5):
         return TRUE



def is_night():
    parameters = {
        "lat": MY_LAT ,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data =response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    #print(sunrise)
    time_now = datetime.now().hour
    #print(time_now.hour)
    if time_now <= sunrise or time_now >= sunset:
        return TRUE
 

while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        send_message()





# latlong.net website search your current location