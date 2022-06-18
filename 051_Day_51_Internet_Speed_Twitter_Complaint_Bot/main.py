# ====================================IMPORTS==================================== #



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from dotenv import load_dotenv
import os



# ====================================CONSTANTS==================================== #



load_dotenv(r'G:\Main\Development\100DaysOfPython\051_Day_51_Internet_Speed_Twitter_Complaint_Bot\.env')

PROMISED_DOWN = 0
PROMISED_UP = 0
CHROME_DRIVER_PATH = "G:\Main\Development\100DaysOfPython\051_Day_51_Internet_Speed_Twitter_Complaint_Bot\venv\Lib\site-packages\chromedriver.exe"
SPEED_TEST_URL = "speedtest.net"
TWITTER_URL = "https://twitter.com/"
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")



# ====================================WEBDRIVER VARIABLES==================================== #



chrome_driver_path = r"G:\Main\Development\100DaysOfPython\050_Day_50_Auto_Tinder_Swiping_Bot\venv\Lib\site-packages\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
tinder = driver.current_window_handle

driver.get(TWITTER_URL)
time.sleep(2)


# ====================================MAIN LOGIC==================================== #


# Click the sign in button
try:
    sign_in_button = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="loginButton"]')
    sign_in_button.click()
    print(f"{sign_in_button.text} Button Pressed")
except ElementClickInterceptedException: 
    sign_in_button = driver.find_element(By.CSS_SELECTOR, 'span[role="button"]')
    print(f"{sign_in_button.text} Alternate Button Pressed")

# fill in user name and press next button
time.sleep(1)
email_field = driver.find_element(By.NAME, "text")
email_field.send_keys(TWITTER_EMAIL)

next_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
next_button.click()
print(f"{next_button.text} Button Pressed")

# username = driver.find_element(By.NAME, "email")
# username.send_keys(facebook_username)
# password = driver.find_element(By.NAME, "pass")
# time.sleep(2)
# password.send_keys(facebook_password, Keys.ENTER)