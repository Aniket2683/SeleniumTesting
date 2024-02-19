from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class handle_dynamicXpath():
    def demo_dynamicPath(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        for i in range(1,6):
            # we concat the dynamic part using "+dynamic+" and then
            # as in py we cannot concat str and number ,therefor we typecast i
            xpath_text = "(//div[@class ='widget LinkList']//a)["+str(i)+"]"
            time.sleep(2)
            driver.find_element(By.XPATH,xpath_text).click()
            time.sleep(2)
            driver.back()
        time.sleep(2)
        driver.quit()

demo1 =handle_dynamicXpath()
demo1.demo_dynamicPath()
