from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Demo_JS_SendKeys():
    def handle_JSsendkeys(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        # JS way is a bit faster than selenium.
        # Note : It is for education purpose ,in real-time  we use Selenium way only.
        # In some rare cases if, Selenium way fails, we can use JS way
        search_box = driver.find_element(By.XPATH,"//input[@title='search']")
        driver.execute_script("arguments[0].value='Selenium'",search_box)
        time.sleep(4)


        driver.quit()

demo1 = Demo_JS_SendKeys()
demo1.handle_JSsendkeys()