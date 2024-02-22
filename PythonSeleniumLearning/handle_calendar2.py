from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class handle_calendar2():
    def calendar2_demo(self):
        driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.guru99.com/test/")
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.NAME,"bdaytime").send_keys("08262003")
        driver.find_element(By.NAME,"bdaytime").send_keys(Keys.TAB)
        driver.find_element(By.NAME,"bdaytime").send_keys("1050")
        driver.find_element(By.NAME, "bdaytime").send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(3)
        driver.quit()

demo1 = handle_calendar2()
demo1.calendar2_demo()


