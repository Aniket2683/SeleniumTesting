# Clicking source code of a webpage

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testpages.eviltester.com/styled/basic-web-page-test.html")
driver.maximize_window()

time.sleep(3)

htmlcode = driver.page_source
# printing code in console
print(htmlcode)
time.sleep(2)

driver.quit()
