import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class DemoJSAlert():
    def JSAlert_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
        time.sleep(2)
        # Alert popped up now we should handle it

        info_alert = driver.switch_to.alert

        print(info_alert.text)
        # to click OK in the Alert
        info_alert.accept()
        time.sleep(2)
        if(driver.find_element(By.ID,"result").is_displayed()):
            print(driver.find_element(By.ID,"result").text)
        driver.quit()


dsw = DemoJSAlert()
dsw.JSAlert_demo()