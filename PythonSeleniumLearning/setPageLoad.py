import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class DemoSetpageLoadTimeout():
    def loading_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # If the page doesn't load in the given time then throw error
        driver.set_page_load_timeout(3)
        driver.get("https://tutorialsninja.com/demo/")

        driver.quit()


dsw = DemoSetpageLoadTimeout()
dsw.loading_demo()