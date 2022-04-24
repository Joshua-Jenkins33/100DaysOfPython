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
# could've stored this in a tuple
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
        # could've done dictionary comprehension here
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