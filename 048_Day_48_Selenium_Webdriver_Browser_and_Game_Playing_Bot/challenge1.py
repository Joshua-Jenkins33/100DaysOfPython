from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r"chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
event_time_whole = driver.find_elements(By.CSS_SELECTOR, "div.event-widget div.shrubbery ul.menu li time")
event_names = driver.find_elements(By.CSS_SELECTOR, "div.event-widget div.shrubbery ul.menu a")

print("++++++++++++++++WHOLE EVENT TIME++++++++++++++++")
[print(item.get_attribute("datetime")) for item in event_time_whole]
print("++++++++++++++++EVENT NAMES++++++++++++++++")
[print(item.text) for item in event_names]


print("++++++++++++++++CREATING LIST++++++++++++++++")
events_dict = {}
the_key = 0

for item in event_time_whole:
    events_dict[str(the_key)] = {
        'time': item.get_attribute("datetime")[:10],
        'name': ''
    }
    the_key +=1

the_key = 0
for item in event_names:
    events_dict[str(the_key)]['name'] = item.text
    the_key +=1

print(events_dict)

driver.quit()