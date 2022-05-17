import requests
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, endpoint, api_key, headers):
        self.endpoint = endpoint
        self.api_key = api_key
        self.headers = headers
        

    def get_iata_code_by_city_name(self, city_name):
        locations_query_endpoint = f"{self.endpoint}/locations/query"
        search = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=locations_query_endpoint, params=search, headers=self.headers)
        response.raise_for_status()
        iata_code = response.json()['locations'][0]['code']
        return iata_code


    def get_flight_price(self, flight_data: FlightData, arrival_city, data_manager):
        flight_search_endpoint = f"{self.endpoint}/v2/search"
        parameters = {
            "fly_from": flight_data.departure_city_code,
            "fly_to": arrival_city,
            "date_from": flight_data.search_date_start,
            "date_to": flight_data.search_date_end,
            "nights_in_dst_from": flight_data.return_flight_min_max_days[0],
            "nights_in_dst_to": flight_data.return_flight_min_max_days[1],
            "flight_type": flight_data.flight_type,
            "one_for_city": 1,
            "max_stopovers": flight_data.max_stopovers,
            "curr": flight_data.currency
        }
        response = requests.get(url=flight_search_endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()

        try:
            price = response.json()["data"][0]['price']
        except IndexError:
            print(f"No flights found for {arrival_city}.")
            return None

        flight_data.price = price
        flight_data.vacation_start_date = response.json()["data"][0]["route"][0]['local_arrival'][:10]
        flight_data.vacation_end_date = response.json()["data"][0]["route"][1]['local_departure'][:10]
        flight_data.arrival_city = response.json()["data"][0]['cityTo']
        print(f"{arrival_city}: ${flight_data.price}")

        notification_manager = NotificationManager(flight_data, data_manager)
        if notification_manager.to_notify:
            notification_manager.send_message()


        return flight_data.price
