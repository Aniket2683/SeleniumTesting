import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class Demo_newWindow():
    def window_demo(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com")
        print(driver.title)
        parent_window = driver.current_window_handle
        time.sleep(3)

        driver.switch_to.new_window('window')

        driver.get("https://selenium143.blogspot.com/")
        print(driver.title)
        windows = driver.window_handles
        # getting all active windows handle

        for w in windows:
            driver.switch_to.window(w)
            if driver.title.__eq__("Selenium143"):
                print(driver.find_element(By.XPATH,"//a[text()='What is Selenium?']"))
                time.sleep(3)
                driver.switch_to.new_window('tab')
                driver.get("https://youtube.com/")
                print(driver.title)
                driver.close()
                break

        driver.switch_to.window(parent_window)
        print(driver.title)

        driver.quit()


dsw = Demo_newWindow()
dsw.window_demo()