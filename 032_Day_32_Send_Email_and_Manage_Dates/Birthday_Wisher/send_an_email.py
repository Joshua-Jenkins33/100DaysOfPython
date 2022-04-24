import smtplib
from dotenv import load_dotenv
from os import getenv

# the dotenv (.env) file keeps my credentials hidden and secure
load_dotenv(r'032_Day_32_Send_Email_and_Manage_Dates\Birthday_Wisher\.env')
EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')
RECEIVER = getenv('RECEIVER')


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls() #Transport Layer Security; makes it secure so interceptors would get encrypted messages
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL, 
        to_addrs=RECEIVER, 
        msg="Subject:Hello!\n\nThis is the body of my email."
    )

# connection.close() # Not needed if you use the `with` keyword again!