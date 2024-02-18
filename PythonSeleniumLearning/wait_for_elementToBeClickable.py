from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Demo_clickable():
    def waitforClick_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//button[text()='Check this']").click()

        wait = WebDriverWait(driver,15)
        checkbox_field = wait.until(expected_conditions.element_to_be_clickable((By.ID,"dte")))
        checkbox_field.click()
        time.sleep(3)
        driver.quit()
dw = Demo_clickable()
dw.waitforClick_demo()
