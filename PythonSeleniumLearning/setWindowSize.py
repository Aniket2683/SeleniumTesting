import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class DemoSetWindowSize():
    def setWindowDemo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        time.sleep(2)
        driver.set_window_size(400,600)
        time.sleep(2)
        driver.quit()


dsw = DemoSetWindowSize()
dsw.setWindowDemo()