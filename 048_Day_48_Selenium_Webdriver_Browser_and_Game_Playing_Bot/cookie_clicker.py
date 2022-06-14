from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

class Store:
    def __init__(self) -> None:
        self.store_ids = ['buyCursor', 'buyGrandma', 'buyFactory', 'buyMine', 'buyShipment', 'buyAlchemy\ lab', 'buyPortal', 'buyTime\ machine']
        self.cursor_price = self.get_prices()[0]
        self.grandma_price = self.get_prices()[1]
        self.factory_price = self.get_prices()[2]
        self.mine_price = self.get_prices()[3]
        self.shipment_price = self.get_prices()[4]
        self.alchemy_lab_price = self.get_prices()[5]
        self.portal_price = self.get_prices()[6]
        self.time_machine_price = self.get_prices()[7]


    def get_prices(self):
        prices = []
        for store_id in self.store_ids:
            prices.append(driver.find_element(By.CSS_SELECTOR, f"div#{store_id} b").text.split(" ")[-1].replace(',',''))
        return prices

        
def fresh_store():
    return Store()

def get_money():
    return int(driver.find_element(By.ID, "money").text.replace(",",""))

def click_cookie():
    driver.find_element(By.ID, "cookie").click()
    print(get_money())

def get_cps():
    return driver.find_element(By.ID, "cps").text

def shop():
    driver.find_element(By.ID, "buyCursor").click()
    print("Bought a cursor")
    number_of_cursors = driver.find_element(By.CSS_SELECTOR, 'div#buyCursor, div.amount').text.split("\n")[0].split(" ")[-1] # this doesn't exist until you buy one otherwise it gets the cost of the cursor
    print(f"Cursors: {number_of_cursors}")

money = get_money()

play_game = True

timeout = time.time() + 10 #60*5   # 5 minutes from now
time_to_shop = time.time() + 5

while play_game:
    click_cookie()

    if time.time() > time_to_shop:
        store = fresh_store()
        shop()
        time_to_shop = time.time() + 5
    if time.time() > timeout:
        play_game = False
     
print(f"The final score was: {get_cps()}")
    
driver.quit()
#     pass