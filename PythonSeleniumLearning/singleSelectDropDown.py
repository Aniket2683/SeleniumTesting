from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time

class DemoDropDownSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.salesforce.com/au/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dropdown = driver.find_element(By.NAME, "UserTitle")
        dd = Select(dropdown)

        dd.select_by_index(1)
        time.sleep(1)

        dd.select_by_visible_text("IT Manager")
        time.sleep(1)
        dd.select_by_value("Operations_Manager_AP")
        time.sleep(1)


Demo = DemoDropDownSelect()
Demo.demo_dropdown()