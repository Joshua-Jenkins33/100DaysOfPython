# ====================================IMPORTS==================================== #



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from dotenv import load_dotenv
import os



# ====================================WEBDRIVER VARIABLES==================================== #



chrome_driver_path = r"G:\Main\Development\100DaysOfPython\049_Day_49_Automating_Job_Applications_on_LinkedIn\venv\Lib\site-packages\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3075033946&f_AL=true&f_E=3&f_JT=F&f_WT=2&keywords=python%20developer")



# ====================================ENVIRONMENT VARIABLES==================================== #



load_dotenv(r'G:\Main\Development\100DaysOfPython\049_Day_49_Automating_Job_Applications_on_LinkedIn\.env')
linkedin_username=os.getenv("LINKEDINUSERNAME")
linkedin_password=os.getenv("LINKEDINPASSWORD")


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

time.sleep(3)
listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

for listing in listings:
    listing.click()
    time.sleep(2)
    save_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
    save_button.click()
    print(f"{save_button.text} Button Clicked!")


    # scroll to the bottom of the right rail
    right_rail = driver.find_element(By.CLASS_NAME, "jobs-search__right-rail")
    right_rail.click()
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    time.sleep(1)

    # follow button
    try:
        follow_button = driver.find_element(By.CSS_SELECTOR, 'button.follow')
        follow_button.click()
        print(f"{follow_button.text} Button Clicked!")
    except NoSuchElementException:
        continue