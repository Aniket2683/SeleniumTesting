import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# infobar is thee thing that says Chrome is controllede by Automation tool....
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension",False)
chrome_options.add_argument('--disable-blink-feature=AutomationControlled')
class Demo_handle_infobar():
    def infobar_demo(self):
        driver = webdriver.Chrome(options= chrome_options,service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://letcode.in/frame")
        driver.maximize_window()
        time.sleep(3)
        driver.quit()
# now you will not see the infobar in top

dsw = Demo_handle_infobar()
dsw.infobar_demo()