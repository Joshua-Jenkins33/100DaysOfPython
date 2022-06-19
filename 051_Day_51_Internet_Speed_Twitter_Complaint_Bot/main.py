# ====================================IMPORTS==================================== #



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
import time
from dotenv import load_dotenv
import os



# ====================================CONSTANTS==================================== #



load_dotenv(r'G:\Main\Development\100DaysOfPython\051_Day_51_Internet_Speed_Twitter_Complaint_Bot\.env')

PROMISED_DOWN = 200
PROMISED_UP = 5
CHROME_DRIVER_PATH = "G:\Main\Development\100DaysOfPython\051_Day_51_Internet_Speed_Twitter_Complaint_Bot\venv\Lib\site-packages\chromedriver.exe"
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login"
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")



# ====================================WEBDRIVER VARIABLES==================================== #



chrome_driver_path = r"G:\Main\Development\100DaysOfPython\050_Day_50_Auto_Tinder_Swiping_Bot\venv\Lib\site-packages\chromedriver.exe"



# ====================================CLASSES==================================== #
class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        time.sleep(2)
        go_button = self.driver.find_element(By.CSS_SELECTOR, "a.js-start-test")
        go_button.click()
        print(f"{go_button.text} Button Pressed.")

        time.sleep(45)

        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE)
        print("Closing Modal")

        self.down = float(self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text)
        print(f"Actual Down: {self.down}")
        self.up = float(self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text)
        print(f"Actual Up: {self.up}")

        
    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(2)

        # fill in user name and press next button
        email_field = self.driver.find_element(By.NAME, "text")
        email_field.send_keys(TWITTER_EMAIL)

        # grab "next" button from list of buttons
        try:
            login_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
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
            email_field = self.driver.find_element(By.NAME, "text")
            email_field.send_keys(TWITTER_USERNAME, Keys.ENTER)
            time.sleep(1)

        # login!
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(TWITTER_PASSWORD, Keys.ENTER)

        time.sleep(2)

        message = f"Hey @xfinity @comcast, why is my internet speed {self.down}down/{self.up}up when I pay for 200down/5up?"
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/compose/tweet"]')
        tweet_button.click()
        print(f"{tweet_button.text} Button Pressed.")

        time.sleep(1)

        tweet_input = self.driver.find_element(By.CSS_SELECTOR, "div.public-DraftEditor-content")
        tweet_input.send_keys(message)
        tweet_button_send = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButton"]')
        tweet_button_send.click()
        print("Tweet Sent!")
            



# ====================================MAIN LOGIC==================================== #

internet_speed_twitter_bot = InternetSpeedTwitterBot()

internet_speed_twitter_bot.get_internet_speed()

if internet_speed_twitter_bot.down < PROMISED_DOWN:
    internet_speed_twitter_bot.tweet_at_provider()
else:
    print("Your Internet speed looks great. Have a nice day.")
