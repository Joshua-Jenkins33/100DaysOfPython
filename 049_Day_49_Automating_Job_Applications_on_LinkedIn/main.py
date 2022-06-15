# ====================================IMPORTS==================================== #



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

# print(os.path.relpath('G:\Main\Development\100DaysOfPython\chromedriver.exe', 'G:\Main\Development\100DaysOfPython\049_Day_49_Automating_Job_Applications_on_LinkedIn\main.py'))
#python -c "import sys; print('\n'.join(sys.path))"


# ====================================WEBDRIVER VARIABLES==================================== #



chrome_driver_path = r"G:\Main\Development\100DaysOfPython\049_Day_49_Automating_Job_Applications_on_LinkedIn\venv\Lib\site-packages\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3075033946&f_AL=true&f_E=3&f_JT=F&f_WT=2&keywords=python%20developer")



# ====================================ENVIRONMENT VARIABLES==================================== #



load_dotenv(r'G:\Main\Development\100DaysOfPython\049_Day_49_Automating_Job_Applications_on_LinkedIn\.env')
linkedin_username=os.getenv("USERNAME")
linkedin_password=os.getenv("PASSWORD")


# ====================================MAIN LOGIC==================================== #


# go to sign in page
time.sleep(1)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# fill credentials and sign in
time.sleep(1)
username = driver.find_element(By.NAME, "session_key")
username.send_keys(linkedin_username)
password = driver.find_element(By.NAME, "session_password")
password.send_keys(linkedin_password, Keys.ENTER)

