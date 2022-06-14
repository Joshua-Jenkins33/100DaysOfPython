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

## Challenge: Use Selenium to Scrape Website Data

## Challenge: Use Selenium in a Blank Project and Scrape a Difference Piece of Data

## How to Automate Filling Out Forms and Clicking Buttons with Selenium

## Cookie Clicker Project

## Challenge: Create an Automated Game Playing Bot