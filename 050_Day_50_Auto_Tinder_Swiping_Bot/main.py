# ====================================IMPORTS==================================== #



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from dotenv import load_dotenv
import os



# ====================================WEBDRIVER VARIABLES==================================== #



chrome_driver_path = r"G:\Main\Development\100DaysOfPython\050_Day_50_Auto_Tinder_Swiping_Bot\venv\Lib\site-packages\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
tinder = driver.current_window_handle

driver.get("https://tinder.com/")



# ====================================ENVIRONMENT VARIABLES==================================== #



load_dotenv(r'G:\Main\Development\100DaysOfPython\050_Day_50_Auto_Tinder_Swiping_Bot\.env')
facebook_username=os.getenv("FACEBOOKUSERNAME")
facebook_password=os.getenv("FACEBOOKPASSWORD")
phone_number=os.getenv("PHONENUMBER")


# ====================================MAIN LOGIC==================================== #

# go to sign in page
time.sleep(1)
sign_in_button = driver.find_element(By.CSS_SELECTOR, "header a.button")
if sign_in_button.text.strip().lower() == "log in":
    sign_in_button.click()

time.sleep(2)
list_of_log_in_buttons = driver.find_elements(By.CSS_SELECTOR, "div span button.button")
for button in list_of_log_in_buttons:
    if "facebook" in button.text.strip().lower():
        button.click()

# fill credentials and sign in
time.sleep(1)

for handle in driver.window_handles:
    print(f"Handle: {handle}\n")
    if handle != tinder:
        login_page = handle

driver.switch_to.window(login_page)

username = driver.find_element(By.NAME, "email")
username.send_keys(facebook_username)
password = driver.find_element(By.NAME, "pass")
time.sleep(2)
password.send_keys(facebook_password, Keys.ENTER)

try:
    time.sleep(6)
    for handle in driver.window_handles:
        if handle != tinder or handle != login_page:
            phone_verification = handle

    driver.switch_to.window(phone_verification)

    phone = driver.find_element(By.NAME, "phone_number")
    phone.send_keys(phone_number, Keys.ENTER)
except:
    print("Didn't need to supply my phone number.")

time.sleep(3)

driver.switch_to.window(tinder)

try:
    location_allow_button = driver.find_element(By.CSS_SELECTOR, "div.onboarding__modal button.button")
    location_allow_button.click()
    time.sleep(2)
    # handle notifications about matches
    buttons = driver.find_elements(By.CSS_SELECTOR, "div button")
    for button in buttons:
        if "not interested" in button.text.strip().lower():
            button.click()
            print("Button Clicked: Not interested in notifications.")
        if "i accept" in button.text.strip().lower():
            button.click()
            print("Button Clicked: Accepted Cookies.")
except:
    print("Didn't need to click location buttons.")

for _ in range(1, 20):
    time.sleep(1)
    buttons = driver.find_elements(By.CSS_SELECTOR, "button.button")
    for button in buttons:
        if "nope" in button.text.strip().lower():
            try:
                button.click()
                print("Button Clicked: Not interested in this profile")
            except ElementClickInterceptedException:
                buttons = driver.find_elements(By.CSS_SELECTOR, "button.button")
                for button in buttons:
                    if "not interested" in button.text.strip().lower():
                        button.click()
                        print("Button Clicked: Not interested in this pop up.")
