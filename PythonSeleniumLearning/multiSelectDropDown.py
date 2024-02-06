from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time

class DemoDropDownMultiSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.mobiscroll.com/jquery/select/multiple-select#")
        # Website not working
        dropdown = driver.find_element(By.NAME, "multiple-select-select")
        dd_multi = Select(dropdown)

        dd_multi.select_by_index(1)
        time.sleep(1)

        dd_multi.select_by_visible_text("Home, Garden & Tools")
        time.sleep(1)
        dd_multi.select_by_value("5")
        time.sleep(1)


Demo = DemoDropDownMultiSelect()
Demo.demo_dropdown()