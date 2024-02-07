import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class Demo_doubleClick():
    def doubleClick_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        rand_element = driver.find_element(By.ID,"testdoubleclick")
        action = ActionChains(driver)
        action.double_click(rand_element).perform()

        # after double click a drop down menu appears

        time.sleep(3)

        driver.quit()


dsw = Demo_doubleClick()
dsw.doubleClick_demo()