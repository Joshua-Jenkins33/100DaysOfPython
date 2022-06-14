# ====================================IMPORTS==================================== #



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time



# ====================================WEBDRIVER VARIABLES==================================== #



chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")



# ====================================CLASSES==================================== #



class Store:
    def __init__(self) -> None:
        self.stock = [
            {
                'id': 'buyCursor',
                'price': 0
            },
            {
                'id': 'buyGrandma',
                'price': 0
            },
            {
                'id': 'buyFactory',
                'price': 0
            },
            {
                'id': 'buyMine',
                'price': 0
            },
            {
                'id': 'buyShipment',
                'price': 0
            },
            {
                'id': 'buyAlchemy\ lab',
                'price': 0
            },
            {
                'id': 'buyPortal',
                'price': 0
            },
            {
                'id': 'buyTime\ machine',
                'price': 0
            }
        ]
        self.update_stock_prices()


    # ====================================STORE METHODS==================================== #

    def update_stock_prices(self):
        for stock_item in self.stock:
            stock_item['price'] = int(driver.find_element(By.CSS_SELECTOR, f"div#{stock_item['id']} b").text.split(" ")[-1].replace(',',''))
        

class User:
    def __init__(self) -> None:
        self._money = 0
        
    # ====================================USER METHODS==================================== #

    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, new):
        self._money = new
    


# ====================================FUNCTIONS==================================== #



def click_cookie(user):
    driver.find_element(By.ID, "cookie").click()
    user.money = int(driver.find_element(By.ID, "money").text.replace(",",""))
    print(user.money)


def get_cps():
    return driver.find_element(By.ID, "cps").text


def buy_item(id):
    # purchase = driver.find_element(By.CSS_SELECTOR, f"#{id}")
    # purchase.click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, id)))
    #TODO: This isn't working; there is a bug here. Element doesn't exist on the page yet for some reason
    print(f"======================================================{element.text}======================================================")
    element.click()


def get_most_expensive_affordable_item(user: User, store: Store):
    for item in reversed(store.stock):
        if user.money >= item['price']:
            print(item['id'])
            buy_item(item['id'])
            # money should be subtracted with the next click of the cookie


def tally_assets(store):
    assets = []
    for item in store.stock:
        print(item)
        try:
            assets.append({'id': item['id'], 'amount': driver.find_element(By.CSS_SELECTOR, f"#{item['id']} amount").text.replace(",","")})
        except NoSuchElementException:
            print(f"Your assets do not include {item['id']}")
    [print(item) for item in assets]



# ====================================MAIN LOGIC==================================== #



user = User()

play_game = True

timeout = time.time() + 60*5   # 5 minutes from now
time_to_shop = time.time() + 5

while play_game:
    click_cookie(user)

    if time.time() > time_to_shop:
        store = Store()
        get_most_expensive_affordable_item(user, store)
        time_to_shop = time.time() + 5
    if time.time() > timeout:
        play_game = False
     
#TODO: For a later date
#tally_assets(store)
    
print("=======================================================")
print(f"The final score was: {get_cps()} Cookies per Second")
print("=======================================================")
driver.quit()
