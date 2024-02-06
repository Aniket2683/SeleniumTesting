# Clicking Forward and back arrow of webBrowser

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "onlytestingblog").click()
time.sleep(3)

driver.back()

time.sleep(2)

driver.forward()
time.sleep(2)

driver.quit()