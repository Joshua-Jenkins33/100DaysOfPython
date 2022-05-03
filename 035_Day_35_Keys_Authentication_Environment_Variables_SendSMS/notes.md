# Day 35: Intermediate+ Keys, Authentication & Environment Variables: Send SMS

## What is API Authentication and Why Do We Need to Authenticate Ourselves?

We've learned about API Endpoints (URL we need to hit up in order to get a particular piece of data), API Parameters (Passing in different inputs so that we can get different pieces of data back from the API provider).

Now we're going to look into using APIs that require authentication. Previously, all APIs we've used have been **free** APIs. We can access all parts of it without payment. The data contained in those APIs are very simple; no one is going to be using that data to build a fancy and commercial application.

Some companies sell access to APIs, like weather. 

### Why Do People Charge for APIs?

How do you even get the weather without using some website or tool? 

OpenWeatherMap has access to over 4000 weather stations across the globe. Their data scientists will take that weather data and look at the satellite images and process that data in order to figure out the weather and predict the weather for cities across the world. Lots of employees, server maintenance, electricty bills, etc. 

Companies thus, sell their data. Especially if someone is going to rely on it heavily to build a commercial app or company.

Most allow you to have a free tier to test things. It only makes sense to charge when you have lots of users.

### API Key

This is how they prevent people from abusing the free tier. The API provider can track how much you're using their API and can deny you access. It's like a password and username tied to you.

## Using API Keys to Authenticate and Get the Weather from OpenWeatherMap

Whenever we use a new API, it's really important to read the documentation. [openweathermap.org](openweathermap.org/api).

There are various options with their own API endpoints. 

Let's try to get the current weather data for the city that we're in.

1. Create an Account at [openweathermap.org](openweathermap.org)
2. Get Your API Key
3. Save it in `main.py` temporarily with a variable
4. Test out the test api call `https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}`
5. Discover that you have to wait a few hours for the API key to be active

### Challenge: One Call API

[latlong.net](latlong.net)

1. Get your latitude and longitude from latlong.net
2. Make a request to the One Call API using the requests module
3. Print out the HTTP status code that you get back
4. Print the response to the console
5. Copy-paste the response to an online JSON viewer (e.g., [jsonviewer.stack.hu](jsonviewer.stack.hu))
6. Locate the hourly forecast for the next 48 hours

```py
import requests

api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

parameters: dict[float, float, str] = {
    "lat": 39.2929292, # SPOOFED
    "lon": -20.15132, # SPOOFED
    "appid": api_key
}

def hit_api():
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    print(response.status_code)
    print(response)
    response.raise_for_status()
    data = response.json()
    print(data)

question_data = hit_api()
```

## Challenge - Check if it Will Rain in the Next 12 Hours

[ventusky.com](ventusky.com) -- this website shows you where it's presently raining.

**Objective:** print `"Bring an Umbrella"` if any of the next 12 hourly weather condition codes is less than 700.

*Hints*
1. Practice printing out the weather ID for the weather in the 0th hour
2. Try to create a slice from the weather data to get a list of hourly forecasts for only the next 12 hours
3. Using the above try to create a list of only the next 12 weather condition codes

```py
def slice_weather_data_to_next_twelve_hours(weather_data: dict) -> list:
  weather_data_hourly = weather_data['hourly']
  twelve_hour_slice = [(index, weather_hour) for (index,weather_hour) in enumerate(weather_data_hourly) if index < 12]
  return twelve_hour_slice

def get_next_twelve_hours_of_weather_condition_codes(weather_data: dict) -> list:
  weather_data_hourly = weather_data['hourly']
  twelve_hour_slice = [weather_hour['weather'][0]['id'] for (index,weather_hour) in enumerate(weather_data_hourly) if index < 12]
  # better way to do that is: weather_data_hourly[:12]
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
  print("Bring an Umbrella!")
```

**Instructor Code**
```py
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
  condition_code = hour_data["weather"][0]["id"]
  if int(condition_code) < 700:
    will_rain = True

if will_rain:
  print("Bring an umbrella.")
```

## Sending SMS via the Twilio API
An API service that allows us to send text message or phone calls or have a virtual phone number in any country; there's a whole bunch of things you can do with the twilio API; ordering system, create a video app, SMS to email, lots of things.

Head to Docs --> QuickStarts --> Programmable SMS Quickstart (Python)

```py
from twilio.rest import Client

account_sid = ''
auth_token = ''

if will_rain:
  client = Client(account_sid, auth_token)
  message = client.messages \
    .create(
      body="It's going to rain today. Remember to bring an ☂️",
      from="TRIAL_NUMBER",
      to="WHO_THE_MESSAGE_WILL_BE_SENT_TO"
    )
  print(message.status)
```

## Use PythonAnywhere to Automate the Python Script
Same as the EMAIL SMS lesson, but there's some tweaks you need to make for free PythonAnywhere accounts (you need to use a Proxy Server)

## Understanding Environment Variables and Hiding API Keys

**Environment Variables.** 2 major use-cases.
1. Convenience
  - Deploying a large application means a large, complicated process. Once it's done, you don't want to update stuff. Instead, you can change the Environment variables. Certain variables being used in your codebase could be set as environment variables. You could modify these without touching your code.
2. Security
  - Usually not a good idea to have things like authentication keys and API keys to be stored in the same place as your code; allows us to separate out where we store our secret stuff away from where our codebase is located.
  - If we *were* to upgrade our account, we'd want to keep these things secret.

Create an environment variable by typing `export OWM_API_KEY=KEY_HERE_NO_QUOTES`
Running `env` in the terminal, you'll see the environment variable.
To tap into the environment variable, you have to `import os`.

```py
api_key = os.environ.get("OWM_API_KEY")
```

### Challenge
Create an environment variable called `AUTH_TOKEN`.
Save the value of the `auth_token` under this environment variable.
Change the code to use the `os` module to retreive the environment variables' value.
Run the `main.py` file to ensure that the program still works.