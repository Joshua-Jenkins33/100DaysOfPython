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

INSTAGRAM_URL = "https://www.instagram.com/"
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
SIMILAR_ACCOUNT = ""



# ====================================WEBDRIVER VARIABLES==================================== #



CHROME_DRIVER_PATH = "G:\Main\Development\100DaysOfPython\052_Day_52_Instagram_Follower_Bot\venv\Lib\site-packages\chromedriver.exe"



# ====================================CLASSES==================================== #