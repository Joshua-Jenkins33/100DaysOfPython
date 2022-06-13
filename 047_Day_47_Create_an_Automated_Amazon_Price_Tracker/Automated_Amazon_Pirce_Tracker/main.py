import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
from os import getenv
from datetime import date


#TODO: Use the requests library to request the HTML page of the Amazon product using the URL

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
ACCEPT_LANGUAGE = "en-US,en;q=0.5"

threshold_price = 350.00

product_url = "https://www.amazon.com/Garmin-Forerunner-Premium-Triathlon-Smartwatch/dp/B07QTVMWVL/ref=sr_1_3?keywords=garmin+forerunner+945&qid=1654989217&sprefix=garmin+fore%2Caps%2C145&sr=8-3"
headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(product_url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")

span_price = soup.select(".a-price-whole,.a-price-fraction")[0:2]
price = ""
for tag in span_price:
    price += tag.getText()

print(f"=================TODAY'S PRICE IS ${price}=================")

price=float(price)

if price < threshold_price:
    load_dotenv(r'047_Day_47_Create_an_Automated_Amazon_Price_Tracker\Automated_Amazon_Pirce_Tracker\.env')
    EMAIL = getenv('EMAIL')
    PASSWORD = getenv('PASSWORD')
    RECEIVER = getenv('RECEIVER')

    date = date.today()
    subj=f"{date} - Amazon Special Item LOW PRICE ALERT"
    message_text=f"From: {EMAIL}\nTo: {RECEIVER}\nSubject: {subj}\nDate: {date}\n\nHello there! Just your friendly homebrewed amazon price checker here to let you know that your item found here:\n\n{product_url}\n\nis on sale and has dropped beneath your threshold price of <b>${round(threshold_price, 2)}</b> to a get-it-while-it's-hot <b>${price}</b>."

    try:
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL,PASSWORD)
        server.sendmail(EMAIL, RECEIVER, message_text)
        server.quit()
        print("Email has been sent!")
    except:
        print("Email didn't send. Something went wrong.")

