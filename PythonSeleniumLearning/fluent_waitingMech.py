import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

class Demo_wait():
    def fluent_demo(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()

        driver.find_element(By.CLASS_NAME,"dropbtn").click()
        # Note : Fluent wait is advanced Explicit wait
        # it is not used in real time
        wait = WebDriverWait(driver,timeout=10,poll_frequency=5,ignored_exceptions=[NoSuchElementException])
        flipkart_option = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Flipkart")))
        # returns a web element

        flipkart_option.click()
        time.sleep(3)
        driver.quit()


demo1 = Demo_wait()
demo1.fluent_demo()
