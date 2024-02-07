import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class Demo_rightClick():
    def rightClick_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/p/page3.html")
        driver.maximize_window()
        rand_element = driver.find_element(By.ID,"multiselect1")
        action = ActionChains(driver)
        action.context_click(rand_element).perform()
        # if you don't provide a web element in above action then it performs the right click on top left(origin)
        time.sleep(3)

        driver.quit()


dsw = Demo_rightClick()
dsw.rightClick_demo()