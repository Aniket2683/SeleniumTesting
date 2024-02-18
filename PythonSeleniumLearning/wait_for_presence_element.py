import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions

class Demo():
    def demo1(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")

        wait = WebDriverWait(driver,30)
        # presence of element is used for elements that are hidden in dom,even if it is not visible on the webpage
        hidden_button = wait.until(expected_conditions.presence_of_element_located((By.ID,"hbutton")))
        print(hidden_button.get_attribute("value"))
        time.sleep(3)
        driver.quit()

dw= Demo();
dw.demo1()