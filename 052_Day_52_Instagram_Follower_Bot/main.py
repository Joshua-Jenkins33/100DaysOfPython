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



load_dotenv(r'G:\Main\Development\100DaysOfPython\052_Day_52_Instagram_Follower_Bot\.env')

INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
SIMILAR_ACCOUNT = ""



# ====================================WEBDRIVER VARIABLES==================================== #



CHROME_DRIVER_PATH = "G:\Main\Development\100DaysOfPython\052_Day_52_Instagram_Follower_Bot\venv\Lib\site-packages\chromedriver.exe"



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
        username_field.send_keys(INSTAGRAM_PASSWORD, Keys.ENTER)


    def find_followers(self):
        pass


    def follow(self):
        pass



# ====================================MAIN LOGIC==================================== #



insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()