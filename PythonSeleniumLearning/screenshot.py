import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class DemoScreenShort():
    def screenshortdemo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
        time.sleep(2)
        # driver.save_screenshot("sceenshotLoginpage.png")

        # By absolute path
        # driver.get_screenshot_as_file("D:\\Python\\Selenium\\PythonSeleniumLearning\\demo_screenshots\\login-page.png")
        # driver.save_screenshot("D:\\Python\\Selenium\\PythonSeleniumLearning\\demo_screenshots\\loginsave.png")

        # By name
        # driver.get_screenshot_as_file("demo_screenshots\\login-name.png")

        time.sleep(2)
        driver.quit()


dsw = DemoScreenShort()
dsw.screenshortdemo()