from twilio.rest import Client
from dotenv import load_dotenv
from pprint import pprint
import smtplib
import os

load_dotenv(r'040_Day_40_Flight_Code_Part_2\flight-deals-end\.env')

TWILIO_SID=os.getenv('TWILIOSID')
TWILIO_AUTH_TOKEN=os.getenv('TWWILIOAUTHTOKEN')
TWILIO_NUMBER=os.getenv('TWILIOPHONE')
MY_PHONE=os.getenv('DESTINATIONPHONE')
SENDER_EMAIL=os.getenv('EMAIL')
SENDER_EMAIL_PASSWORD=os.getenv('PASSWORD')


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_PHONE,
        )
        # Prints if successfully sent.
        print(f"Message's Status: {message.status}")


    def send_emails(self, emails: list, message: str, google_flight_link):
        pprint(emails)
        pprint(message)

        
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=SENDER_EMAIL,
                    to_addrs=email,
                    msg=message
                )

