# Day 37: Intermediate+ Habit Tracking Project: API Post Requests & Headers

## HTTP Post Requests

**GET** `requests.get()` -- parameters go inside the paranthesis
**POST** `.post()`
**PUT** `.put()`
**DELETE** `.delete()`

A POST request is where we give the external system a piece of data and we're not so interested in the response we're getting back other than whether it was successful or not. Posting data into a google sheet or post a tweet to twitter.

PUT is where you update a piece of data in the external service; updating values in a spreadsheet.

DELETE is where you want to delete a piece of data in the external service like a facebook post or a tweet.

We need to POST to the pixela API. We'll be posting data to Pixela to be tracked in our graph.

Pixela has a "short form get started guide" that has six steps to accomplishing it.

### Setting up a User Account on Pixela
```py
import requests

USERNAME = "SOME_USER_NAME"
TOKEN = "SOME_TOKEN_LIKE_AN_API_KEY_YOU_GENERATE"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
```

## Advanced Authentication using an HTTP Header

### Create a Graph Definition

This is the second of six steps listed on the pixela documentation.

```py
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
  "id": "graph1",
  "name": "Swimming Graph",
  "unit": "Yd",
  "type": "float",
  "color": "sora"
}

requests.post(url=graph_endpoint, json=graph_config)
```

### Headers

Like letters, headers are the part that contains relevant pieces of information like phone numbers, website, logo whereas the body is the message part that changes from letter to letter.

These can prevent sniffing and intercepting from happening. HTTPS can protect you but there are cases where your API key can still be leaked.

```py
headers = {
  "X-USER-TOKEN": TOKEN
}

requests.post(url=graph_endpoint, json=graph_config, headers=headers)
```

Now we can view it by navigating to the link contained on step 3 and replacing the username with our own and add a `.html` at the end.

## Challenge: Add a Pixel to the Habit Tracker using a Post Request
Comment out the code where you create the graph. Then use the documentation to post a Pixel to your habit graph for the date when you are taking this lesson. You should see your new pixel displayed when you refresh the website.

```py
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

body = {
    "date": "20220504",
    "quantity": "1400"
}

# requests.post(url=pixel_creation_endpoint, json=body, headers=headers)
print(response.text)

requests.delete(url=f'{pixel_creation_endpoint}/20200504', headers=headers)
```

## Autofilling today's date using strftime

```py
from datetime import date

today = datetime.now()
today = datetime(year=2020, month=7, day=23)
print(today) # not in the format I need it to be

pixel_data = {
  "date": today.strftime("%Y%m%d"),
  "quantity": "1400"
}
```

### Challenge
Make sure you have posted at least two data points to the graph already (e.g., today and yesterday). Updated yesterday's data point to a new value using an HTTP put request. Refresh the chart on your website to check that your update was successful.

**PUT/UPDATE**
```py
update_data = {
  "quantity": 800
}

endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220506"

requests.put(url=endpoint, json=updated_data, headers=headers)
```
## How to use HTTP Put and Delete Requests

```py
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220506"
requests.delete(url=delete_endpoint, header=headers)
print(requests.text)
```