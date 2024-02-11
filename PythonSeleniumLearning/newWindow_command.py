import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class Demo_newWindow():
    def window_demo(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com")
        print(driver.title)
        time.sleep(3)

        driver.switch_to.new_window('window')

        driver.get("https://selenium143.blogspot.com/")
        print(driver.title)


        driver.switch_to.new_window('tab')

        driver.get("https://youtube.com/")
        print(driver.title)
        driver.close()

        driver.quit()


dsw = Demo_newWindow()
dsw.window_demo()