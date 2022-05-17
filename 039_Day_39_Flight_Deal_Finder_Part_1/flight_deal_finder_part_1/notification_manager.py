from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv(r'039_Day_39_Flight_Deal_Finder_Part_1\flight_deal_finder_part_1\.env')

TWILIO_SID=os.getenv('TWILIOSID')
TWILIO_AUTH_TOKEN=os.getenv('TWWILIOAUTHTOKEN')
TWILIO_NUMBER=os.getenv('TWILIOPHONE')
MY_PHONE=os.getenv('DESTINATIONPHONE')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_data, data_manager):
        self.flight_data = flight_data
        self.data_manager = data_manager
        self.sheet_price = self.data_manager.get_price_by_location(self.flight_data.arrival_city)
        self.flight_price = self.flight_data.price
        self.to_notify = self.check_for_low_flight_price()


    
    def check_for_low_flight_price(self) -> bool:
        if self.flight_price <= self.sheet_price:
            print("You should buy this ticket")
            return True
        else:
            return False

    
    def send_message(self):
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
        .create(
            body=f"Headline: Low price alert! \
                \nOnly ${self.flight_data.price} to fly from {self.flight_data.departure_city}-{self.flight_data.departure_city_code} to {self.flight_data.arrival_city}-{self.flight_data.arrival_city_code}, from {self.flight_data.vacation_start_date} to {self.flight_data.vacation_end_date}.",
            from_=TWILIO_NUMBER,
            to=MY_PHONE
        )
        print(message.status)