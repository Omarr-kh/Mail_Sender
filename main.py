import random
import pandas
from datetime import datetime as dt
import smtplib

EMAIL = "email"
PASS = "pass"

today = (dt.now().month, dt.now().day)


birthdays_data = pandas.read_csv("./birthdays.csv")
birthdays_dict = {(data["month"], data["day"]): data for (
    i, data) in birthdays_data.iterrows()}

if today in birthdays_dict:
    person_data = birthdays_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as f:
        letter = f.read()
        letter = letter.replace("[NAME]", person_data["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=person_data["email"], 
            msg=f"Subject:Happy Birthday\n\n{letter}"
            )
        print(letter)
