import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class DemoSizeAndLocationOfElement():
    def sizeAndlocation_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://tutorialsninja.com/demo/")
        time.sleep(2)
        serchbox_size_loc= driver.find_element(By.XPATH,"//input[@placeholder='Search']").rect
        print(serchbox_size_loc)
        time.sleep(2)
        driver.quit()


dsw = DemoSizeAndLocationOfElement()
dsw.sizeAndlocation_demo()