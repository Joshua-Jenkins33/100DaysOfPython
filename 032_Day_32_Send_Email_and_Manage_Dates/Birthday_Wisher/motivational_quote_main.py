import smtplib
from dotenv import load_dotenv
from os import getenv
import datetime as dt
from random import choice

load_dotenv(r'032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\.env')
EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')
RECEIVER = getenv('RECEIVER')
QUOTE_PATH = r'032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\quotes.txt'
SEND_ON_THIS_WEEKDAY = 0 #Monday

def send_email(body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=EMAIL, 
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