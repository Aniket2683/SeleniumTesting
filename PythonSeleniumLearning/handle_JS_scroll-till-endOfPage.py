from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class Demo_JS_Scroll():
    def handle_JSscroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        time.sleep(3)
        # Note : There is no direct command in Selenium to scroll until end of page.
        # Hence, we use JS for it
        scroll_height = str(driver.execute_script(" return document.documentElement.scrollHeight"))
        driver.execute_script("window.scrollTo(0,"+scroll_height+")")
        time.sleep(3)
        driver.quit()
demo1 = Demo_JS_Scroll()
demo1.handle_JSscroll()