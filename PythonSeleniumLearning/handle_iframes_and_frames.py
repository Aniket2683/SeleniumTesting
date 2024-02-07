import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
class Demoframes_iframes():
    def iframes_frames_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/iframe")
        driver.maximize_window()
        driver.switch_to.frame("mce_0_ifr")
        time.sleep(3)
        driver.find_element(By.XPATH,"//body/p").clear()
        time.sleep(3)
        driver.quit()


dsw = Demoframes_iframes()
dsw.iframes_frames_demo()