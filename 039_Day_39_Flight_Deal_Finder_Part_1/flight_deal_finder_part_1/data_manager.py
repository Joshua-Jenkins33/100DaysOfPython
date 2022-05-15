from pprint import pprint
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, endpoint, headers):
        self.endpoint = endpoint
        self.headers = headers
        self.data = requests.get(url=self.endpoint, headers=self.headers)
        self.data.raise_for_status()


    def get_prices(self):
        data = self.data.json()
        return data['prices']


    def update_iata_code(self, row_data, id):
        put_endpoint = f"{self.endpoint}/{id}"
        row_input = {
            "price": {
                "iataCode": row_data['iataCode']
            }
        }

        response = requests.put(url=put_endpoint, json=row_input, headers=self.headers)
        response.raise_for_status()
        print(response.text)


"""
  sheet_inputs = {
    "workout": {
      "date": date,
      "time": time,
      "exercise": exercise['name'].title(),
      "duration": exercise["duration_min"],
      "calories": exercise["nf_calories"]
    }
  }
"""
