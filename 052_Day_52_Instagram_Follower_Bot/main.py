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

        remember_creds_button = self.driver.find_element(By.CSS_SELECTOR, "button.sqdOP")
        print(f"{remember_creds_button.text} Button Pressed.")
        remember_creds_button.click()

        # remember_creds_not_now_button = self.driver.find_element(By.CSS_SELECTOR, "div.cmbtv button")
        # print(f"{remember_creds_not_now_button.text} Button Pressed.")
        # remember_creds_not_now_button.click()

        time.sleep(5)

        notification_not_now_button = self.driver.find_element(By.CSS_SELECTOR, "button._a9--._a9_1")
        print(f"{notification_not_now_button.text} Button Pressed.")
        notification_not_now_button.click()

        time.sleep(1)


    def find_followers(self):
        time.sleep(5)
        self.driver.get(SIMILAR_ACCOUNT)

        time.sleep(2)
        followers=self.driver.find_element(By.PARTIAL_LINK_TEXT,'followers')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.CSS_SELECTOR, 'div.qg4pu3sx.flebnqrf.kzt5xp73.h98he7qt.e793r6ar.pi61vmqs.od1n8kyl.h6an9nv3.j4yusqav')
        for i in range(10):
            #In this case we're executing some Javascript, that's what the execute_script() method does. 
            #The method can accept the script as well as a HTML element. 
            #The modal in this case, becomes the arguments[0] in the script.
            #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop + arguments[0].offsetHeight;", modal)
            time.sleep(2)

        
    def follow(self):
        max_follows = 150
        current_follows = 0
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            if current_follows >= max_follows:
                break
            else:
                if button.text.strip().lower() == 'follow':
                    button.click()
                    print(f"{button.text} Button Pressed.")
                    time.sleep(1)
                    current_follows += 1
                else:
                    print("You're already following this account.")



# ====================================MAIN LOGIC==================================== #



insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()