import requests
from dotenv import load_dotenv
from os import getenv
from datetime import date, timedelta
from twilio.rest import Client
import re

load_dotenv(r'036_Day_36_Stock_Trading_News_Alert_Project\stock-news-extrahard-start\.env')
ALPHA_ADVANTAGE_API_KEY=getenv('ALPHAADVANTAGEAPIKEY')
NEWS_API_KEY=getenv('NEWSAPIKEY')
TWILIO_SID=getenv('TWILIOSID')
TWILIO_AUTH_TOKEN=getenv('TWWILIOAUTHTOKEN')
TWILIO_NUMBER=getenv('TWILIOPHONE')
DESTINATION_NUMBER=getenv('DESTINATIONPHONE')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DELTA = 0.02

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# ===================================www.alphavantage.co API CALL============================================================
parameters = {
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK,
    "apikey": ALPHA_ADVANTAGE_API_KEY,
    "datatype": "json"
}

url = 'https://www.alphavantage.co/query'
response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()
# ===========================================================================================================================

def handle_market_closures(data: dict, date1: date, date2: date):
    """The API data doesn't contain key-value pairs for dates where the market is closed. This means we can't just yesterday and the day before in our code; we have to have a way to bounce back to the date closest to that.

    Args:
        data (dict): the json response from www.alphavantage.co/query using the parameters contained in this document
        date1 (date): yesterday's date
        date2 (date): the day before yesterday's date

    Returns:
        day_1_data: the value of the associated date key from the alphavantage api, using date1 as the key
        day_2_data: the value of the associated date key from the alphavantage api, using date2 as the key
    """
    while str(date1) not in data:
        # print(f"The market was closed on {date1}. Going back 1 day.")
        date1 -= timedelta(days=1)

    while str(date2) not in data:
        # print(f"The market was closed on {date2}. Going back 1 day.")
        date2 -= timedelta(days=1)

    if date1 == date2:
        date2 -= timedelta(days=1)

    # print(f"\nWe are using the following date as \"yesterday's\" date: {date1}")
    # print(f"We are using the following date as \"the day before yesterday's\" date: {date2}")

    return data[str(date1)], data[str(date2)]


def get_daily_stock_delta(most_recent_data: dict, older_data: dict) -> float:
    """Take the difference between two dates from the alphavantage api using the value at closing time and use that different to get the percentage change.
    If that percentage change is greater than our determined value, then it's considered a significant change.

    Args:
        most_recent_data (dict): alphavantage api object, drilled down to the date key's value
        older_data (dict): alphavantage api object, drilled down to the date key's value

    Returns:
        bool: whether or not the delta between the two prices of the stock is significant
    """
    difference = float(most_recent_data['4. close']) - float(older_data['4. close'])
    delta: float = difference/float(older_data['4. close'])
    # print(f"\nDelta: {delta}")
    
    return delta


yesterday = date.today() - timedelta(days=1)
day_before_yesterday = yesterday - timedelta(days=1)

#print(f"\nYesterday was: {yesterday}\nAnd the day before yesterday was: {day_before_yesterday}\n")

day_1_data, day_2_data = handle_market_closures(data['Time Series (Daily)'], yesterday, day_before_yesterday)

delta: float = get_daily_stock_delta(day_1_data, day_2_data)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# ===================================www.newsapi.org API CALL================================================================
from_date = list(day_2_data.keys())[0]
to_date = list(day_1_data.keys())[0]

def get_news(from_date: str, to_date: str)->list:
    """hit newsapi.org and get the first three articles related to the pre-set company

    Args:
        from_date (str): used in the api call to dynamically assign the oldest articles to consider in the news search
        to_date (str): used i nthe api call to dynamically assign the newest articles to consider in the news search

    Returns:
        list: returns a list of three article dictionaries
    """
    parameters = {
        "q": COMPANY_NAME,
        "from": from_date,
        "to": to_date,
        "language": 'en',
        # "sortBy": "publishedAt",
        "apikey": NEWS_API_KEY
    }

    url = 'https://newsapi.org/v2/everything'
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    news_data = response.json()

    return news_data['articles'][0:3]
# ===========================================================================================================================

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def clean_brief(brief: str) -> str:
    CLEAN_REGEX = re.compile('<.*?>')
    clean_text = re.sub(CLEAN_REGEX, '', brief)
    clean_text = clean_text.split('.')[0]
    return clean_text

if abs(delta) > DELTA:
    articles = get_news(from_date=from_date, to_date=to_date)
    print_delta: str = f"{'????' if delta > 0 else '????'}{str(round(delta*100, 0))}%"

    headline1 = articles[0]['title']
    brief1 = clean_brief(articles[0]['description'])

    headline2 = articles[1]['title']
    brief2 = clean_brief(articles[1]['description'])

    headline3 = articles[2]['title']
    brief3 = clean_brief(articles[2]['description'])



    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
            body=f"{STOCK}: {print_delta}\nHeadline: {headline1}\nBrief: {brief1}\n\nHeadline: {headline2}\nBrief: {brief2}\n\nHeadline: {headline3}\nBrief: {brief3}",
            from_=TWILIO_NUMBER,
            to=DESTINATION_NUMBER
        )
    print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: ????2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: ????5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

