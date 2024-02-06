import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
class DemoDropdown():
    def dropdown_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        drop_down_field= driver.find_element(By.ID,"drop1")

        select_option = Select(drop_down_field)
        print(select_option.is_multiple)
        select_option.select_by_value("def")
        time.sleep(2)
        select_option.select_by_index(2)
        time.sleep(2)
        select_option.select_by_visible_text("doc 3")

        drop_down_options= select_option.options

        for option in drop_down_options:
            print(option.text)

        driver.quit()


dsw = DemoDropdown()
dsw.dropdown_demo()