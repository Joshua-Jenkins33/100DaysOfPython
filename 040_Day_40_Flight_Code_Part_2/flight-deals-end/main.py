import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

load_dotenv(r'040_Day_40_Flight_Code_Part_2\flight-deals-end\.env')

FLIGHT_DEALS_TOKEN=os.getenv("FLIGHTDEALSTOKEN")
SHEETY_ENDPOINT = 'https://api.sheety.co/f5343720735630e16f47193195b5f6d9/flightDeals'
SHEETY_HEADERS = {"Authorization": f"Bearer {FLIGHT_DEALS_TOKEN}"}

data_manager = DataManager(SHEETY_ENDPOINT, SHEETY_HEADERS)
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "DEN"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight == None:
        continue
    else:
        if flight.price < destination["lowestPrice"]:
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            if flight.stop_overs > 0:
                message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."
        
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(data_manager.get_emails(), message, link)