from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Demo_JS_Clicks():
    def handle_JSclicks(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()

        # Selenium click
        # driver.find_element(By.ID,"alert1").click()
        # time.sleep(3)

        # # JS click (Type 1)
        # driver.execute_script("document.getElementById('alert1').click()")
        # time.sleep(3)

        # JS click (Type 2)
        button = driver.find_element(By.ID,"alert1")
        driver.execute_script("arguments[0].click()",button)
        time.sleep(3)

        driver.quit()

demo1 = Demo_JS_Clicks()
demo1.handle_JSclicks()