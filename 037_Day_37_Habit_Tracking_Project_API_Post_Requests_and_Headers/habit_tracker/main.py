import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# TODO: Separate out into functions
# TODO: Create user prompts for information

load_dotenv(r'037_Day_37_Habit_Tracking_Project_API_Post_Requests_and_Headers\habit_tracker\.env')

USERNAME=os.getenv("USERNAME")
TOKEN=os.getenv("TOKEN")
GRAPH_ID="graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Swimming Graph",
    "unit": "Yd",
    "type": "float",
    "color": "sora"
}

requests.post(url=graph_endpoint, json=graph_config)

headers = {
    "X-USER-TOKEN": TOKEN
}

# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

body = {
    "date": today,
    "quantity": "120"
}

# requests.post(url=pixel_creation_endpoint, json=body, headers=headers)
print(response.text)

# requests.delete(url=f'{pixel_creation_endpoint}/20200504', headers=headers)
put_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_data = {
    "date": today,
    "quantity": input("How many yards did you actually swim today?")
}
requests.put(url=put_url, json=update_data, headers=headers)
print(response.text)