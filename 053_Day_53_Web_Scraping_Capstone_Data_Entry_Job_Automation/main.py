# ====================================IMPORTS==================================== #



from audioop import add
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os
from pprint import pprint
import re



# ====================================CONSTANTS==================================== #



FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSftMVw-f6kPBYdlk7evZesod-3YGrojaIwhI28kS5Holf2ayg/viewform?usp=sf_link"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
ACCEPT_LANGUAGE = "en-US,en;q=0.5"
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}



# ====================================FUNCTIONS==================================== #



def strip_price_to_digits(price: str) -> int:
  return int(re.sub('\D', '', price))


def create_full_zillow_link(zillow_link: str) -> str:
  if ".com" not in zillow_link:
    zillow_link = f"https://www.zillow.com{zillow_link}"
  return zillow_link



# ====================================MAIN VARIABLES==================================== #



response = requests.get(ZILLOW_LINK, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')

addresses = soup.find_all("address", class_="list-card-addr")
prices = soup.find_all(class_="list-card-price")
links = soup.find_all("a", class_="list-card-img", href=True)
properties = []


chrome_driver_path = r"C:\repos\100DaysOfPython\053_Day_53_Web_Scraping_Capstone_Data_Entry_Job_Automation\venv\Lib\site-packages\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(FORM_LINK)



# ====================================MAIN LOGIC==================================== #



# ------------------------------------WEBSCRAPING------------------------------------ #
if len(addresses) == len(prices) and len(addresses) == len(links):
  print("===EVERYTHING LOOKS GOOD; CONTINUING===")

  number_of_properties = len(addresses)
  for _ in range(number_of_properties):
    address = addresses[_].contents[0]
    price = strip_price_to_digits(prices[_].contents[0])
    link = create_full_zillow_link(links[_]['href'])

    properties.append(
      {
        "address": address,
        "price": price,
        "link": link
      }
    )
    print(f"Property {_+1} Parsed")
  print("===EXTRACTING DATA COMPLETE===")
  print(properties)
else:
  print("===WEBSCRAPING DID NOT RESULT IN THE SAME NUMBER OF ELEMENTS; TERMINATING.===")


# ------------------------------------FILLING FORMS------------------------------------ #
print("===CONTINUING TO FILL FORMS===")

for property in properties:
  text_fields = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")

  address_field = text_fields[0]
  address_field.send_keys(property['address'])

  price_field = text_fields[1]
  price_field.send_keys(property['price'])

  link_field = text_fields[2]
  link_field.send_keys(property['link'])

  submit_button = driver.find_element(By.CSS_SELECTOR, 'div[role="button"].uArJ5e.UQuaGc')
  submit_button.click()
  print("Property posted! Next Property...\n")

  time.sleep(2)

  # should have some logic to check if this is the last element
  new_form_link = driver.find_element(By.CSS_SELECTOR, "div.c2gzEf a")
  new_form_link.click()
  print("Filling in a new form...")
  