import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class DemoHTMLtag_name():
    def tagnamedemo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://yatra.com/")
        time.sleep(2)
        TOE = driver.find_element(By.CLASS_NAME,"main-heading").tag_name
        print(TOE)
        time.sleep(2)
        driver.quit()


dsw = DemoHTMLtag_name()
dsw.tagnamedemo()