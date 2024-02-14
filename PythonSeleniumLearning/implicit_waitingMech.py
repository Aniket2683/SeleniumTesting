from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

class Demo_waiting():
    def wait_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        # wait for max 10 sec before throwing an exception
        # it is a global wait ,it waits for all the elements on the webpage
        driver.find_element(By.CLASS_NAME,"dropbtn").click()
        driver.find_element(By.LINK_TEXT,"Flipkart").click()

        time.sleep(3)
        driver.quit()

demo1 = Demo_waiting()
demo1.wait_demo()