import smtplib
import datetime 
import pandas
import random

PLACEHOLDER ="[NAME]"

my_email = "terslyparadise@gmail.com"
password = "ndkabesfainbdzxo"

# Check if today matches a birthday in the birthdays.csv

today_month = datetime.datetime.now().month
today_day = datetime.datetime.now().day
today = (today_month, today_day)

# Read data from csv 

data = pandas.read_csv("BirthdayWisher/birthdays.csv")
birthdays_dic = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows() }
# check if today exists in the birthday dictionary
if today in birthdays_dic:
    birthday_person = birthdays_dic[today]["name"]
    file_path = f"BirthdayWisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(PLACEHOLDER, birthday_person)
        print(birthday_person)
        print(contents)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_dic[today]["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )












# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="terslyparadise@yahoo.com",
#         msg="Subject:hello\n\nThis is the body of email"
#     )

# now = datetime.datetime.now()
# weekday = now.weekday()

# if weekday == 1:
#     with open(file="BirthdayWisher/quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#     print(quote)

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=my_email,
#             msg=f"Subject:Monday Motivation\n\n{quote}"
#         )