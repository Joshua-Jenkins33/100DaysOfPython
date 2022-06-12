import requests
import lxml
from bs4 import BeautifulSoup


#TODO: Use the requests library to request the HTML page of the Amazon product using the URL

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
ACCEPT_LANGUAGE = "en-US,en;q=0.5"

product_url = "https://www.amazon.com/Garmin-Forerunner-Premium-Triathlon-Smartwatch/dp/B07QTVMWVL/ref=sr_1_3?keywords=garmin+forerunner+945&qid=1654989217&sprefix=garmin+fore%2Caps%2C145&sr=8-3"
headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(product_url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")