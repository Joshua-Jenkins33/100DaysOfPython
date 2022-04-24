# Day 32: Intermediate+ Send Email (smtplib) & Manage Dates (datetime)
We're going to learn how to send an email using python code and when we send this email using the `datetime` module. We're going to build an **Automated Birthday Wisher.**

**Email SMTP** comes pre-bundled with Python and allows us to send emails using Python code.
**datetime** is another Python module that helps us format dates and figure out what today is, etc.

## A Note About the Next Lesson: Google SMTP Port
In the next lesson, I'll show you how to send email using the `smtplib` module and Python. If you are getting the error Connection unexpectedly closed, it might be due to a number of things. You can come back to this lesson to debug.

1. Make sure you've got the correct smtp address for your email provider:

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com

If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"



Below are steps specific to users sending email from Gmail addresses.

2. Make sure you've enabled less secure apps if you are sending from a Gmail account. (Refer to the video in the next lesson for steps).

3. Try to go through the [Gmail Captcha here](https://accounts.google.com/DisplayUnlockCaptcha) while logged in to the Gmail account

4. Add a port number by changing your code to this:

`smtplib.SMTP("smtp.gmail.com", port=587) `

## How to Send Emails with Python using SMTP

### How Does Email Work?
What happens behind the scenes?

We have a **sender**: angela@gmail.com
And a **recipient**: timmy@yahoo.com+

There's a Gmail Mail Server (which will send the message) and a Yahoo Mail Server (which will store the message) until Timmy logs onto his computer, logs onto Yahoo.com, which downloads the email from the Yahoo Mail Server.

This relies on the **SMTP.** The **S**imple **M**ail **T**ransfer **P**rotocol. This contains all rules for how an email is received by a mail server, passed onto the next mail server, and how email can be sent around the internet.

Analogies: Mail Servers are the Post Offices. Timmy's Computer is his mailbox. SMTP is the postman that knows how to deliver Timmy's mail to Timmy.

### Writing an Email in Python!
```py
import smtplib
from dotenv import load_dotenv
from os import getenv

# the dotenv (.env) file keeps my credentials hidden and secure
load_dotenv(r'032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\.env')
EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')
RECEVIER = getenv('RECEIVER')


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls() #Transport Layer Security; makes it secure so interceptors would get encrypted messages
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL, 
        to_addrs=RECEVIER, 
        msg="Subject:Hello!\n\nThis is the body of my email."
    )

# connection.close() # Not needed if you use the `with` keyword again!
```

## Working with the datetime Module
Helps us work with dates and time!

```py
import datetime as dt

now = dt.datetime.now()
print(now)

# This date is very specific and hard to work with.
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

if year == 2020:
    print("Wear a face mask")
print(type(now))

date_of_birth = dt.datetime(year=1995,month=12,day=15, hour=7)
print(date_of_birth)
```

## Challenge 1 - Send Motivational Quotes on Mondays via Email
**Objective.** Send a motivational quote via email on the current weekday (you can change it to Monday afterwards)

*Hints:*
1. Use the `datetime` module to obtain the current day of the week.
2. Open the `quotes.txt` file and obtain a list of quotes.
3. Use the `random` module to pick a random quote from your list of quotes.
4. Use the `smtplib` to send the email to yourself.

```py
import smtplib
from dotenv import load_dotenv
from os import getenv
import datetime as dt
from random import choice

load_dotenv(r'032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\.env')
EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')
RECEIVER = getenv('RECEIVER')
QUOTE_PATH = r'G:\Main\Development\100DaysOfPython\032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\quotes.txt'
SEND_ON_THIS_WEEKDAY = 0 #Monday

def send_email(body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=RECEIVER, 
            msg=f"Subject:Monday's Motivational Quote!\n\n{body}"
        )


def get_quote():
    with open(QUOTE_PATH) as read_file:
        all_quotes = read_file.readlines()
        return choice(all_quotes)
        

now = dt.datetime.now()
if now.weekday() == SEND_ON_THIS_WEEKDAY:
    quote = get_quote()
    send_email(quote)
else:
    print('Not sending the email today.')
```

## Automated Birthday Wisher Project Challenge
```py
import smtplib
from dotenv import load_dotenv
from os import getenv
import datetime as dt
from pandas import *
from random import choice

load_dotenv(r'032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\.env')
EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')
RECEIVER = getenv('RECEIVER')
BIRTHDAY_LIST = r'032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\birthday_files\birthdays.csv'
EMAIL_TEMPLATE_PATHS_LIST = [r'032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\birthday_files\letter_1.txt',r'032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\birthday_files\letter_2.txt',r'032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\birthday_files\letter_3.txt']

birthdays_today = []
now = dt.datetime.now()
day = now.day
month = now.month

def send_birthday_email(person, body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls() 
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=person['email'], 
            msg=f"Subject:Happy Birthday, {person['name']}!\n\n{body}"
        )


def read_in_file_to_dataframe(path):
    with open(path) as read_file:
        return read_csv(read_file)


def get_birthdays_today(dataframe):
    dataframe.reset_index()
    for index, row in dataframe.iterrows():
        if row['month'] == month and row['day'] == day:
            birthdays_today.append(
                {
                    "name": row['name'],
                    "email": row['email']

                }
            )


def select_random_template(path_list):
    template = choice(path_list)
    return template


def fill_template(template_path, person):
    with open(template_path) as read_file:
        all_lines = " ".join(line for line in read_file)
        filled_template = all_lines.replace('[NAME]', str(person['name']))
        return filled_template


birthdays_df = read_in_file_to_dataframe(BIRTHDAY_LIST)

get_birthdays_today(birthdays_df)

for person in birthdays_today:
    template = select_random_template(EMAIL_TEMPLATE_PATHS_LIST)
    filled_template = fill_template(template, person)
    send_birthday_email(person, filled_template)
```

## Solution & Walkthrough for the Automated Birthday Wisher

### Instructor Code
```py
#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

```

## Run Your Python Code in the Cloud!

I can head to [this link](https://www.pythonanywhere.com/user/glynyon/) to automate and schedule executions of my scripts.

Unfortunately, I was unable to install the `dotenv` module on the terminal there.