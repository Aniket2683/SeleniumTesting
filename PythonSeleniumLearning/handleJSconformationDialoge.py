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
        driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
        time.sleep(2)
        # confirmation popped up now we should handle it

        conformation_alert = driver.switch_to.alert

        print(conformation_alert.text)
        # # to click OK in the confirmation
        # conformation_alert.accept()
        # time.sleep(2)
        # if(driver.find_element(By.ID,"result").is_displayed()):
        #     print(driver.find_element(By.ID,"result").text)

        # to click Cancle in the confirmation
        conformation_alert.dismiss()
        time.sleep(2)
        if (driver.find_element(By.ID, "result").is_displayed()):
            print(driver.find_element(By.ID, "result").text)
        driver.quit()


dsw = DemoJSAlert()
dsw.JSAlert_demo()