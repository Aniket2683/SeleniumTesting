from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class Demo_JS_Scroll():
    def handle_JSscroll(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.scrapingbee.com/blog/selenium-python/")
        driver.maximize_window()
        time.sleep(3)
        # Note : There is no direct command in Selenium to scrape a website
        # Hence, we use JS for it
        scraped_text = str(driver.execute_script("return document.documentElement.innerText"))
        time.sleep(3)
        print(scraped_text)
        driver.quit()
demo1 = Demo_JS_Scroll()
demo1.handle_JSscroll()


