from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class Demo_JS_executor():
    def handle_JS(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()

        # executing JS in selenium
        driver.execute_script("alert('Hello From Selenium')")
        alert_box = driver.switch_to.alert
        time.sleep(4)
        alert_box.accept()
        time.sleep(2)


        # driver.execute_script("prompt('What is your name ?')")
        # time.sleep(2)
        # NOTE : send_keys is working but chrome has issue displaying the keys that are send to the alert
        # prompt_box = driver.switch_to.alert
        # prompt_box.send_keys('Aniket Jaiswal')
        # time.sleep(4)
        # prompt_box.accept()

        driver.execute_script("confirm('Are you sure ?')")
        time.sleep(3)
        confirm_box = driver.switch_to.alert
        confirm_box.dismiss()
        driver.quit()

demo1 = Demo_JS_executor()
demo1.handle_JS()
