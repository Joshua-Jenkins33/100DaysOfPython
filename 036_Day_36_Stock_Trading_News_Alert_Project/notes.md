# Day 36: Intermediate+ Stock Trading News Alert Project

## Choose Your Destiny

## Solution & Walkthrough for Step 1 - Check for Stock Price Movements

### Instructor Code
```py
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_EDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "SOMEAPIKEY"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday, then print ("Get News")

#TODO 1. - Get yesterday's closing stock price
stock_params = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK_NAME,
  "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#TODO 2. Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: w3 schools for absolute value.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 5: # change to get it to work
  print("Get News")
```

## Solution & Walkthrough for Step 2 - Get the News Articles

### Instructor Code

```py
NEWS_API_KEY = "SOMEAPIKEY"

#TODO 6. Instead of printing ("Get News"), use the NEWS API to get articles related to the COMPANY_NAME.
# If difference percentage is greater than 5 then print ("Get News")
if diff_percent > 1:
  news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
  }
  news_response = requests.get(NEWS_ENDPOINT, params=news_params)
  articles = new_response.json()["articles"]

#TODO 7. Use Python slice operator to create a list that contains the first 3 articels. Hint: stackoverflow.com : understanding slice notation
three_articles = articles[:3]
```

## Solution & Walkthrough for Step 3 - Send the SMS Messages

### Instructor Code

```py
#TODO 8. Create a new list of the first 3 article's headline and desription using list comprehension
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

#TODO 9. Send each article as a separate message via Twilio
import twilio.rest import Client

TWILIO_SID = "SIDNUMBER"
TWILIO_AUTH_TOKEN = "AUTHTOKEN"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

for article in formatted_articles:
  message = client.messages.create(
    body=article,
    from=TWILIO_NUMBER,
    to=MY_NUMBER
  )

#TODO 10. Check if the difference is negative or positive
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
  up_down = "🔺"
else:
  up_down = "🔻"




if abs(diff_percent) > 1:
#   news_params = {
#     "apiKey": NEWS_API_KEY,
#     "qInTitle": COMPANY_NAME
#   }
#   news_response = requests.get(NEWS_ENDPOINT, params=news_params)
#   articles = new_response.json()["articles"]


formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\n Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

```