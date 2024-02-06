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
        driver.maximize_window()
        driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
        time.sleep(2)
        # prompt popped up now we should handle it
        prompt_alert = driver.switch_to.alert
        print(prompt_alert.text)
        prompt_alert.send_keys("Aniket")
        time.sleep(6)
        prompt_alert.accept()
        # prompt_alert.dismiss()
        time.sleep(3)
        if(driver.find_element(By.ID,"result").is_displayed()):
            print(driver.find_element(By.ID,"result").text)
        driver.quit()


dsw = DemoJSAlert()
dsw.JSAlert_demo()