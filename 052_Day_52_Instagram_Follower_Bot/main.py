# ====================================IMPORTS==================================== #



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os



# ====================================CONSTANTS==================================== #



load_dotenv(r'G:\Main\Development\100DaysOfPython\052_Day_52_Instagram_Follower_Bot\.env')

INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
SIMILAR_ACCOUNT = "https://www.instagram.com/spoonmebaking"



# ====================================WEBDRIVER VARIABLES==================================== #



CHROME_DRIVER_PATH = r"G:\Main\Development\100DaysOfPython\052_Day_52_Instagram_Follower_Bot\venv\Lib\site-packages\chromedriver.exe"



# ====================================CLASSES==================================== #



class InstaFollower:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    
    def login(self):
        self.driver.get(INSTAGRAM_URL)

        time.sleep(1)

        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(INSTAGRAM_USERNAME)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(INSTAGRAM_PASSWORD, Keys.ENTER)

        time.sleep(8)

        remember_creds_not_now_button = self.driver.find_element(By.CSS_SELECTOR, "div.cmbtv button")
        print(f"{remember_creds_not_now_button.text} Button Pressed.")
        remember_creds_not_now_button.click()

        time.sleep(5)

        notification_not_now_button = self.driver.find_element(By.CSS_SELECTOR, "button._a9--._a9_1")
        print(f"{notification_not_now_button.text} Button Pressed.")
        notification_not_now_button.click()

        time.sleep(1)


    def find_followers(self):
        self.driver.get(SIMILAR_ACCOUNT)

        time.sleep(2)

        followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        print(f"{followers_link.text} Link Clicked.")
        followers_link.click()

        time.sleep(1)

        
    def follow(self):
        #successfully executes up to here
        pop_up_window = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div._a3gq")))

        while True:
            follower_list = self.driver.find_elements(By.CSS_SELECTOR, "div._aae- li")
            for follower in follower_list:
                self.follow(follower)
        
            follower_account = self.driver.find_element(By.CSS_SELECTOR, 'a[role="link"] span._aac1').text
            follower_account = follower.text
            print(f"Testing {follower_account}...")
            
            follow_button = self.driver.find_element(By.CSS_SELECTOR, "li button._acan")
            if follow_button.text.strip().lower() == 'follow':
                follow_button.click()
                print(f"{follow_button.text} Button Pressed.")
            else:
                print("You're already following this account.")
            
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window
                )
            time.sleep(1)



# ====================================MAIN LOGIC==================================== #



insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()