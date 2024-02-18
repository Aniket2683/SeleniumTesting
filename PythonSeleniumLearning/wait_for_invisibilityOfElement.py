from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Demo_invisibility():
    def checkIfInvisibility_demo(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//button[text()='Start']").click()

        wait = WebDriverWait(driver,15)
        loading_progress = wait.until(expected_conditions.invisibility_of_element_located((By.ID,"loading")))
        visible_heading= driver.find_element(By.XPATH,"//div[@id='finish']/h4").text
        print(visible_heading)
        driver.quit()
dw = Demo_invisibility()
dw.checkIfInvisibility_demo()