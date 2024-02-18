import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Demo_alert():
    def alertVisible_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()

        driver.find_element(By.ID,"alert1").click()
        # It's always better to wait for alert to appear before performing any operation on it
        wait = WebDriverWait(driver,3)
        wait.until(expected_conditions.alert_is_present())
        # Now that the alert is present on the webpage we can switch to alert and perform operation on it
        visible_alert = driver.switch_to.alert
        print(visible_alert.text)
        time.sleep(3)
        visible_alert.accept()
        time.sleep(1)
        driver.quit()
dw = Demo_alert()
dw.alertVisible_demo()