# Day 48 Selenium Webdriver Browser and Game Playing Bot

## How to Install & Set Up Selenium
Step 1: Install Chrome :(
Step 2: Install Webdriver and create a variable that references its path
Step 3: Install Selenium
- To do this, pip install Selenium
- Then create a webdriver object with the Chrome object using the webdriver executable path: `driver = webdriver.Chrome(executable_path=chrome_driver_path)`

### What is the Webdriver?
We've got out Selenium package which contains code for us to be able to interact with browsers. It can work with many different browsers; we have to create a bridge to a specific browser that bridges Selenium code to work with the Chrome browser. Different drivers for different browsers.

Now we **use** it!

### Using It
`driver.get("https://www.amazon.com")`

This effectively opens up a new browser window with the url we specified. We want to close down the window/browser once we're done automating/doing.

`driver.close()` -- this just closes the active tab
`driver.quit()` -- quits the entire browser; some cases where you have multiple tabs open; preferable


## How to Find and Select Elements on a Website with Selenium
Previous Lesson's Current Code
```py
from selenium import webdriver

chrome_driver_path = r"C:\Main\Applications\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

driver.close()
```

We're going to automate yesterday's task! Replace yesterday's url in the `driver.get()` method.
`driver.get("https://www.amazon.com/Garmin-Forerunner-Premium-Triathlon-Smartwatch/dp/B07QTVMWVL/ref=sr_1_3?keywords=garmin+forerunner+945&qid=1654989217&sprefix=garmin+fore%2Caps%2C145&sr=8-3")`

`price = driver.find_element_by_id("priceToPay")`

The above is deprecated. I had to use [the following](https://selenium-python.readthedocs.io/locating-elements.html):
```py
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r"chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com")
driver.get("https://www.amazon.com/Garmin-Forerunner-Premium-Triathlon-Smartwatch/dp/B07QTVMWVL/ref=sr_1_3?keywords=garmin+forerunner+945&qid=1654989217&sprefix=garmin+fore%2Caps%2C145&sr=8-3")
price = driver.find_element(By.CLASS_NAME, "priceToPay")
item_price = ".".join(price.text.split('\n'))
print(item_price)

driver.quit()
```

Getting elements by name is often used for filling out forms.
```py
driver.get("https://www.python.org/")
# driver.find_element_by_name("q")
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
```

Get the logo
```py
driver.get("https://www.python.org/")
#logo = driver.find_element_by_class_name("python-logo")
logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)
```

**CSS Selector**
Useful when things don't have a class or ID that can be identifiable.
```py
# driver.find_elements_by_css_selector(".documentation-widget a")
driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)
```

**XPATH**
Right click on the element and copy its XPATH.
```py
#driver.find_element_by_xpath("//*[@id="site-map"]/div[2]/div/ul/li[3]/a")
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)
```
## Challenge: Use Selenium to Scrape Website Data

From [python.org](python.org), print a dictionary of the upcoming events.

You'll need to use `find_elements`, plural.

> Extract the upcoming event data from the python.org website. Use Selenium to scrape all upcoming event dates and event names (in my case there are 5) and store them in a nested Python dictionary. Print the dictionary to the console. The event data from python.org should be stored under the keys "time" and "name". 

```py
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
```

### Instructor Code

```py
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
```

## Challenge: Use Selenium in a Blank Project and Scrape a Difference Piece of Data

## How to Automate Filling Out Forms and Clicking Buttons with Selenium

## Cookie Clicker Project

## Challenge: Create an Automated Game Playing Bot