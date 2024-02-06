import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class DemoSizeOfElement():
    def size_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://tutorialsninja.com/demo/")
        time.sleep(2)
        serchbox_size= driver.find_element(By.XPATH,"//input[@placeholder='Search']").size
        print(serchbox_size)
        time.sleep(2)
        driver.quit()


dsw = DemoSizeOfElement()
dsw.size_demo()