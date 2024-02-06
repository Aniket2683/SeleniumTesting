import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
class DemoPushNotification():
    def push_demo(self):
        chrome_option = Options()
        chrome_option.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_option,service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://yatra.com/")
        # now the push notification for loction will not pop up .


        driver.quit()


dsw = DemoPushNotification()
dsw.push_demo()