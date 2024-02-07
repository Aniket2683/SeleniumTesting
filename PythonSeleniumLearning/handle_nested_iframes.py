import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
class Demonested_iframes():
    def iframes_nested_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://letcode.in/frame")
        driver.maximize_window()
        driver.switch_to.frame("firstFr")
        driver.find_element(By.NAME,"fname").send_keys("Aniket")
        driver.find_element(By.NAME,"lname").send_keys("Jaiswal")
        time.sleep(3)
        child_frame = driver.find_element(By.XPATH,"//iframe[@class='has-background-white']")
        driver.switch_to.frame(child_frame)
        driver.find_element(By.NAME,"email").send_keys("jaiswalaniket304@gmail.com")
        time.sleep(3)

        driver.find_element(By.NAME,"email").clear()

        driver.switch_to.parent_frame()
        driver.find_element(By.NAME, "fname").clear()
        driver.find_element(By.NAME, "lname").clear()
        time.sleep(3)

        # now switch to page level from parent level.....you can directly come from child frame as well
        driver.switch_to.default_content()

        page_heading= driver.find_element(By.XPATH,"//div[@class='hero-body']//h1").text
        print(page_heading)
        driver.quit()


dsw = Demonested_iframes()
dsw.iframes_nested_demo()