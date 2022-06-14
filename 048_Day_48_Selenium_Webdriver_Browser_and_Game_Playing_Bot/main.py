from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r"chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com")
driver.get("https://www.amazon.com/Garmin-Forerunner-Premium-Triathlon-Smartwatch/dp/B07QTVMWVL/ref=sr_1_3?keywords=garmin+forerunner+945&qid=1654989217&sprefix=garmin+fore%2Caps%2C145&sr=8-3")
price = driver.find_element(By.CLASS_NAME, "priceToPay")
item_price = ".".join(price.text.split('\n'))
print(item_price)

driver.quit()