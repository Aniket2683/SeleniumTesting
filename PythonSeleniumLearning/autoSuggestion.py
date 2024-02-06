import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeServices
from webdriver_manager.chrome import ChromeDriverManager

class DemoAutoSuggestion():
    def AutoSuggestion(self):
        driver = webdriver.Chrome(service= ChromeServices(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        departure = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        time.sleep(3)
        departure.click()
        time.sleep(3)
        departure.send_keys("New Delhi")
        departure.send_keys(Keys.ENTER)
        time.sleep(3)

        goingto = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        goingto.click()
        goingto.send_keys("New")
        time.sleep(3)
        serch_results = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")

        for result in serch_results:
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(3)
                break

demoAuto = DemoAutoSuggestion()
demoAuto.AutoSuggestion()