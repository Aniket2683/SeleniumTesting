import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class Demo_JS():
    def JS_demo(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com")
        driver.execute_script("alert('hello there')")
        time.sleep(3)
        driver.quit()


dsw = Demo_JS()
dsw.JS_demo()