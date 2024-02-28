from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Demo_JS_Scroll():
    def handle_JSscroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        time.sleep(3)
        # Note : There is no direct command in Selenium to scroll until an element is visible.
        # Hence, we use JS for it
        dropdown_button = driver.find_element(By.CLASS_NAME,"dropbtn")
        driver.execute_script("arguments[0].scrollIntoView(true)",dropdown_button)
        time.sleep(3)
        driver.quit()
demo1 = Demo_JS_Scroll()
demo1.handle_JSscroll()