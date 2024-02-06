import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class DemolocationOfElement():
    def location_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://tutorialsninja.com/demo/")
        time.sleep(2)
        serchbox_loc= driver.find_element(By.XPATH,"//input[@placeholder='Search']").location
        print(serchbox_loc)
        time.sleep(2)
        driver.quit()


dsw = DemolocationOfElement()
dsw.location_demo()