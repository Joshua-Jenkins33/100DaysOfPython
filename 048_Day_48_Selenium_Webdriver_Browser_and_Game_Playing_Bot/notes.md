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

Create a blank file called interaction.py. Use Selenium to print the total number of articles from the Wikipedia homepage to the console.

```py
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r"chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
english_article_count = driver.find_element(By.CSS_SELECTOR, "div#articlecount a").text.replace(',',"")

print(english_article_count)

driver.quit()
```

### Instructor Code
```py
from selenium import webdriver

chrom_driver_path = "yada"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)
```
## How to Automate Filling Out Forms and Clicking Buttons with Selenium
How to interact with the elements we find!

```py
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = r"chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
english_article_count = driver.find_element(By.CSS_SELECTOR, "div#articlecount a")
english_article_count.click()

driver.quit()
```

**Finding by Text**
Deprecated\*
`all_portals = driver.find_element_by_link_text("All portals")`

Supported
`all_portals = driver.find_element(By.LINK_TEXT, 'All portals')`
`all_portals.click()`

### Populating a Search Bar
```py
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_driver_path = r"chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)
# driver.quit()
```

### Challenge 3
Practice using Selenium to fill in [this form](http://secure-retreat-92358.herokuapp.com/) and clicking Sign Up (this is not a real registration page).

```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Jimmy")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Purdue")
email = driver.find_element(By.NAME, "email")
email.send_keys("jimmypurdue@gmail.com")
send_keys(Keys.ENTER)

# driver.quit()
```

Instructor Code
```py
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Jimmy")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Purdue")
email = driver.find_element(By.NAME, "email")
email.send_keys("jimmypurdue@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
```
## Cookie Clicker Project

## Challenge: Create an Automated Game Playing Bot