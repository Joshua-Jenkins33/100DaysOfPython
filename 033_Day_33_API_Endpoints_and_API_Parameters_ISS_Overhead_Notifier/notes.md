# Day 33: Intermediate+ API Endpoints & API Parameters - ISS Overhead Notifier

## What are Application Programming Interfaces (APIs)?

An **Application Programming Interface** (API) is a set of commands, functions, protocols, and objects that programmers can use to create software or *interact with an external system.*

An API is essentially an interface or a barrier between your program and an external system. You're trying to use the rules the API has prescribed to make a request to the external system. If you have met all the requirements posed by the API this external system has set out in their API, this external system will respond to you and deliver data to your request. If you don't follow their rules, your request will be denied and you'll be told to effectively "go away".

The websites are the "restuarant" and thet data is the "kitchen" that powers the websites behind the scenes. 
- It's not appropriate to go to the kitchen
- We have menus; these tell you what you can get from the restaurant.
    - Your tummy is your program
    - The menu is the API; your tummy makes requests to the kitchen through the structure of the menu
    - The kitchen is the external program

### API Examples
- Yahoo Weather
- NBA Stats
- Coinbase

## API Endpoints and Making API Calls
One of the most important aspects of an API is the **API Endpoint** (a location). If you want to get money out of the bank, you have to know where the bank is and go to the bain.

**Coinbase Example.** `api.coinbase.com`

**API Request.** Similar to going to the bank and getting money out. Going to the withdraw data from their vault; world would be chaotic if everyone could go to the bank and get what they needed without any checks and balances; you can't go to the vault by yourself. The bank teller is like the API (between you and the bank vault). You could ask her for money, but she'll ask you questions like to present your ID, what's your account number, etc etc.

You can ask her some questions where she won't need to authenticate, however, like "What are your opening hours?". This is the equivalent of a very simple `GET REQUEST`. 

We'll be using the **International Space Station Current Location** API.
**Endpoint.** `http://api.open-notify.org/iss-now.json` (returns output in form of `.json`)

### JSON

Initially created for JavaScript but then it became the standard for shuttling information between applications across the Internet.

You could create a Python Dictionary, but... we'll use the "Purchase a Dresser" scenario. I can't fit the dresser in my car, but I want to buy it. IKEA solved this issue with the flatpack—it can now fit in your car; you just have to assemble it at home. This flatpack is our JSON. There aren't extra spaces, no indents. It's very basic and minimal. This can be transported across the Internet effectively without much issue due to its small and minimal design.

It can later be reconstituted back into the dresser (Python Dictionary) so you can work with it.

### Make an API Request
```py
import requests #needs to be installed

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)
```

The above code doesn't return the JSON object we were expecting; it returns a `<Response [200]>` value. This is our response code.

## Working with Responses: HTTP Codes, Exceptions & JSON Data

What are the response codes we can get from an API? The most important ones are the ones that tell us if our requests succeeded or failed.
- 404 (The thing you're looking for doesn't exist)
- 1XX: Hold On
- 2XX: Here You Go
- 3XX: Go Away
- 4XX: You Screwed Up
- 5XX: I Screwed Up (I = Server)

### Getting Status Codes

#### Status Code: 200
```py
import requests #needs to be installed

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response.status_code) # Prints only the status code; Prints 200
```

#### Status Code: 400
```py
import requests #needs to be installed

response = requests.get(url="http://api.open-notify.org/is-now.json") # misspell the end point

print(response.status_code) # Prints only the status code; Prints 404
```

#### Raise an Exception for Non-200 Responses
This is an example of a poorly written exception due to its very generic nature and we're just catching a status code whose value is not 200.
```py
import requests #needs to be installed

response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code != 200:
    raise Exception("Bad response from ISS API")
```

**Better Raised Exception**
```py
import requests #needs to be installed

response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code == 404:
    raise Exception("That resources does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorized to access this data.")
```

### Using `response` Module to Raise Exceptions
There are a *lot* of [http status codes](https://www.webfx.com/web-development/glossary/http-status-codes/). You actually don't need to worry about handling those exceptions or creating dozens of if statements. The `request` [module](https://docs.python-requests.org/en/latest/) can generate the exceptions instead. It is **the** most popular way for Python developers to work with APIs.

```py
import requests #needs to be installed

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # if we don't get a 200 (pass), then you'll see an exception being raised and it's quite specific
```

### Now to Actually Get the Data from the Request

```py
import requests #needs to be installed

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data) # now it looks like what we got in our browser!

position_longitude = data["iss_position"]["longitude"]
position_latitude = data["iss_position"]["latitude"]

iss_position = (position_longitude, position_latitude)
```

To see where locations are based on latitude and longitude, we can use a resource called [latlong.net](latlong.net). 
1. You'll got to **Geographic Tools**
2. **Latitude and Longitude to Address**
3. Paste in longitude and latitude values
4. Press convert

## Challenge - Build a Kanye Quotes App using the Kanye Rest API

1. Make a `get()` request to the [Kanye Rest API](https://kanye.rest/)
2. Raise an exception if the request returned an unsuccessful **status code**.
3. Parse the `JSON` to obtain the quote text.
4. Display the quote in the canvas' `quote_text` widget.

```py
def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=f"{data['quote']}")
```

## Understand API Parameters: Match Sunset Times with the Current Time

**API Parameters** allows you to give an input when you're making an API request so that you can get diferrent pieces of data back depending on your input, in the same way that you can give different inputs to a function to get different feedback.

This allows you to ask the bank and, instead of asking "What are your opening hours" (a broadstroak question) and replace it with "What time do you close on {Monday}?"

The `sunrise-sunset` api located at [sunrise-sunset.org/api](sunrise-sunset.org/api) is an example of a more complex API that can take in API Parameters. The ISS Location API is quite simple and doesn't have any parameters.

Here's the **actual API Link**: `https://api.sunrise-sunset.org/json`

### API Documentation

They will usually tell how you should structure your parameters. 

### Goal: Get Sunrise and Sunset Times
The following code will return a 400 error. A 400 error being:
> 400 BAD REQUEST
> "The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).

In our case, we haven't provided the required values!
```py
response = requests.get("https://api.sunrise-sunset.org/json")
response.raise_for_status() 
```

**Fix that by providing values!** The keys must match the ones provided in the documentation.
```py
import requests

MY_LAT = -33.901624
MY_LONG = 18.586511
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status() 
```

We're just interested in the sunrise and sunset times.

**Note.** If you're interested in viewing the data in a bit more structured way (using browser extensions) you can navigate to the url *with* the parameters. You specify that you're using parameters by utilizing a `?`. 

So that would look something like this: `https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400`

**Endpoint** ? **ParamName** = **Value** & **ParamName** = **Value**

```py
import requests
from datetime as dt
MY_LAT = -33.901624
MY_LONG = 18.586511
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status() 
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise) # prints in 12 hour, AM/PM

time_now = dt.now()

print(time_now) # very different format; 24 hour clock format
```

Sunrise-Sunset API has a `formatted` optional parameter that can be turned off or on. Switching the default to off, you can turn it into a unix format.

### Challenge: Modify the API Call
Modify the API call: turn off the formatting and time in the 24;hour style

```py
import requests
from datetime as dt

MY_LAT = -33.901624
MY_LONG = 18.586511

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status() 
sunrise = data["results"]["sunrise"].split("T")[1].split0(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split0(":")[0]

time_now = dt.now()

print(time_now.hour)

```

## ISS Overhead Notifier Project - Challenge & Solution

```py
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )



```