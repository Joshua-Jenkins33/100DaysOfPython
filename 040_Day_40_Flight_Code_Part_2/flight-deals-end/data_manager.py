from pprint import pprint
import requests

class DataManager:

    def __init__(self, endpoint, headers):
        self.destination_data = {}
        self.endpoint = endpoint
        self.headers = headers
        self.sheet_1 = "prices"
        self.sheet_2 = "users"
        self.user_data = self.get_user_data()
        self.email_list = self.get_emails()

    def get_destination_data(self):
        response = requests.get(url=f"{self.endpoint}/{self.sheet_1}", headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    
    def get_user_data(self):
        response = requests.get(url=f"{self.endpoint}/{self.sheet_2}", headers=self.headers)
        data = response.json()
        print(data)
        self.user_data = data["users"]
        return self.user_data


    def get_emails(self):
        emails = []
        for user in self.user_data:
            emails.append(user['email'])
        return emails


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.endpoint}/{self.sheet_1}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            #print(response.text)
