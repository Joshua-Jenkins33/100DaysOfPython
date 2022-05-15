import requests
from flight_data import FlightData
from pprint import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, endpoint, api_key, headers, fly_to=None):
        self.endpoint = endpoint
        self.api_key = api_key
        self.headers = headers
        self.fly_to = fly_to
        

    def get_iata_code_by_city_name(self, city_name):
        locations_query_endpoint = f"{self.endpoint}/locations/query"
        search = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=locations_query_endpoint, params=search, headers=self.headers)
        response.raise_for_status()
        # print(response.json())
        iata_code = response.json()['locations'][0]['code']
        return iata_code


    def get_flight_price(self, flight_data: FlightData, fly_to):
        self.fly_to = fly_to
        print(self.fly_to)
        flight_search_endpoint = f"{self.endpoint}/v2/search"
        parameters = {
            "fly_from": flight_data.departure_city,
            "fly_to": self.fly_to,
            "date_from": flight_data.search_date_start,
            "date_to": flight_data.search_date_end,
            # "nights_in_dst_from": flight_data.return_flight_min_max_days[0],
            # "nights_in_dst_to": flight_data.return_flight_min_max_days[1],
            # "flight_type": flight_data.flight_type,
            # "one_for_city": 1,
            # "max_stopovers": flight_data.max_stopovers,
            # "curr": flight_data.currency
        }
        response = requests.get(url=flight_search_endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()

        if self.get_iata_code_by_city_name("Paris") == "PAR":
            pprint(response.json())


