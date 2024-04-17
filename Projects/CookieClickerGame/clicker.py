import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"promptContentChangeLanguage")))
driver.find_element(By.ID,"langSelect-EN").click()
time.sleep(4)

# Accept cookie
accept_cookie_message = "Got it!"
wait1 = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.LINK_TEXT,accept_cookie_message)))
driver.find_element(By.LINK_TEXT,accept_cookie_message).click()



# Click the cookie

cookie_id = "bigCookie"
cookie = driver.find_element(By.ID,cookie_id)

#  Product price
product_price_prefix = "productPrice"
product_prefix = "product"


# Floating Note
note_prefix = "note-"


while True:
    cookie.click()
    cookie_count = driver.find_element(By.ID,"cookies").text.split(" ")[0]
    cookie_count = int(cookie_count.replace("," , ""))
    try:
        note = driver.find_element(By.XPATH, "//div[@id='notes']//div[contains(@class, 'close')]")
        time.sleep(0.5)
        note.click()
    except NoSuchElementException:
        try:
            # If the above element is not found, try to find the element with id 'upgrades' and data-id '0'
            upgrade = driver.find_element(By.XPATH,"//div[@id='upgrades']//div[@class='crate upgrade enabled']")
            upgrade.click()  # If enabled, click on it
        except NoSuchElementException:
            pass
    for i in range(4):  # because we have 4 products
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue
        product_price = int(product_price)
        if cookie_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break





