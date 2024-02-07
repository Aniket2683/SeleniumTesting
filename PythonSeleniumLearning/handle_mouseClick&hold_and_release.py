import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class Demo_ClickHoldandRelease():
    def clickholdrelease_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://selenium08.blogspot.com/2020/01/click-and-hold.html")
        driver.maximize_window()
        A_element = driver.find_element(By.XPATH,"//li[@name='A']")
        H_element = driver.find_element(By.XPATH,"//li[@name='H']")
        action = ActionChains(driver)
        action.click_and_hold(A_element).move_to_element(H_element).release().perform()
        time.sleep(3)
        # More optimised way is to use drag_and_drop(elem1,elem2).perform()
        driver.quit()


dsw = Demo_ClickHoldandRelease()
dsw.clickholdrelease_demo()