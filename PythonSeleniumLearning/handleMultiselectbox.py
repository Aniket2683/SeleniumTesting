import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
class DemoMultiselectBox():
    def dropdown_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        multiselect_box= driver.find_element(By.ID,"multiselect1")

        select_option = Select(multiselect_box)
        select_option.select_by_index(1)
        time.sleep(2)
        select_option.select_by_value("volvox")
        time.sleep(2)
        select_option.select_by_visible_text("Hyundai")
        print(select_option.is_multiple)
        select_option.deselect_all()

        driver.quit()


dsw = DemoMultiselectBox()
dsw.dropdown_demo()