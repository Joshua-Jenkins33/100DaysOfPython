from selenium import webdriver

chrome_driver_path = r"C:\Main\Applications\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com")
driver.get("https://www.amazon.com/Garmin-Forerunner-Premium-Triathlon-Smartwatch/dp/B07QTVMWVL/ref=sr_1_3?keywords=garmin+forerunner+945&qid=1654989217&sprefix=garmin+fore%2Caps%2C145&sr=8-3")

driver.close()