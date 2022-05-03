import requests
import os
from twilio.rest import Client


api_key = os.environ.get("API_KEY")
number = os.environ.get("TWILIO_NUMBER")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_account_SID = os.environ.get("TWILIO_ACCOUNT_SID")
my_phone = os.environ.get("MY_PHONE")
latitude = os.environ.get("LATITUDE")
longitude = os.environ.get("LONGITUDE")

parameters: dict[float, float, str, str] = {
    "lat": latitude,
    "lon": longitude,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

def hit_api() -> dict:
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    response.raise_for_status()
    weather_data = response.json()
    return weather_data


def get_current_weather_code(weather_data: dict) -> int:
  return weather_data['hourly'][0]['weather'][0]['id']

def slice_weather_data_to_next_twelve_hours(weather_data: dict) -> list:
  weather_data_hourly = weather_data['hourly']
  twelve_hour_slice = [(index, weather_hour) for (index,weather_hour) in enumerate(weather_data_hourly) if index < 12]
  return twelve_hour_slice

def get_next_twelve_hours_of_weather_condition_codes(weather_data: dict) -> list:
  weather_data_hourly = weather_data['hourly']
  twelve_hour_slice = [weather_hour['weather'][0]['id'] for (index,weather_hour) in enumerate(weather_data_hourly) if index < 12]
  return twelve_hour_slice


weather_data = hit_api()
# print(get_current_weather_code(weather_data))
# print(slice_weather_data_to_next_twelve_hours(weather_data))
#print(get_next_twelve_hours_of_weather_condition_codes(weather_data))


twelve_hour_codes = get_next_twelve_hours_of_weather_condition_codes(weather_data)

will_rain_today = False
for hour in twelve_hour_codes:
  if hour < 700:
    will_rain_today = True

if will_rain_today:
  client = Client(twilio_account_SID, twilio_auth_token)
  message = client.messages \
    .create(
      body="It's going to rain today. Remember to bring an ☂️",
      from_=number,
      to=my_phone
    )
  print(message.status)
