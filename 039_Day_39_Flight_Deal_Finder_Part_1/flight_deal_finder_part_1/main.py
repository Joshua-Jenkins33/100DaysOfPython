#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
#import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv(r'039_Day_39_Flight_Deal_Finder_Part_1\flight_deal_finder_part_1\.env')

FLIGHT_DEALS_TOKEN=os.getenv("FLIGHTDEALSTOKEN")
SHEETY_ENDPOINT = 'https://api.sheety.co/f5343720735630e16f47193195b5f6d9/flightDeals/prices'
SHEETY_HEADERS = {"Authorization": f"Bearer {FLIGHT_DEALS_TOKEN}"}

KIWI_ENDPOINT = 'https://tequila-api.kiwi.com'
KIWI_API_KEY=os.getenv("TEQUILAKIWIAPI")
KIWI_HEADERS = {"apikey": KIWI_API_KEY}

data_manager = DataManager(SHEETY_ENDPOINT, SHEETY_HEADERS)
sheet_data = data_manager.get_prices()


for destination in sheet_data:
    flight_search = FlightSearch(KIWI_ENDPOINT, KIWI_API_KEY, KIWI_HEADERS)

    if len(destination['iataCode']) < 1:
        destination['iataCode'] = flight_search.get_iata_code_by_city_name(destination['city'])
        data_manager.update_iata_code(destination, destination['id'])
    
    flight_data = FlightData(destination['iataCode'])
    flight_search.get_flight_price(flight_data, destination['iataCode'], data_manager)
    

