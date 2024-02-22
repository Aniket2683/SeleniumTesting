import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.maximize_window()
driver.execute_script("document.getElementById('datepicker').value='26/08/2024'")
time.sleep(2)
driver.quit()