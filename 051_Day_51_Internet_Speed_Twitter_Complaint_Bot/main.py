# ====================================IMPORTS==================================== #



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
import time
from dotenv import load_dotenv
import os



# ====================================CONSTANTS==================================== #



load_dotenv(r'G:\Main\Development\100DaysOfPython\051_Day_51_Internet_Speed_Twitter_Complaint_Bot\.env')

PROMISED_DOWN = 0
PROMISED_UP = 0
CHROME_DRIVER_PATH = "G:\Main\Development\100DaysOfPython\051_Day_51_Internet_Speed_Twitter_Complaint_Bot\venv\Lib\site-packages\chromedriver.exe"
SPEED_TEST_URL = "speedtest.net"
TWITTER_URL = "https://twitter.com/i/flow/login"
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")



# ====================================WEBDRIVER VARIABLES==================================== #



chrome_driver_path = r"G:\Main\Development\100DaysOfPython\050_Day_50_Auto_Tinder_Swiping_Bot\venv\Lib\site-packages\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
twitter = driver.current_window_handle

driver.get(TWITTER_URL)
time.sleep(2)


# ====================================MAIN LOGIC==================================== #


# fill in user name and press next button
email_field = driver.find_element(By.NAME, "text")
email_field.send_keys(TWITTER_EMAIL)

# grab "next" button from list of buttons
try:
    login_buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for button in login_buttons:
        if button.text.strip().lower() == "next":
            button.click()
            print(f"{button.text} Button Pressed")
            break
        else:
            print('No "NEXT" button exists.')
    time.sleep(2)
# handle "unusual activity"
except StaleElementReferenceException:
    time.sleep(1)
    email_field = driver.find_element(By.NAME, "text")
    email_field.send_keys(TWITTER_EMAIL[:7], Keys.ENTER)
    time.sleep(1)

for handle in driver.window_handles:
    print(f"Handle: {handle}")
    if handle != twitter:
        login_page = handle

# login!
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(TWITTER_PASSWORD, Keys.ENTER)