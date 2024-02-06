import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
class DemoRadioButtonAndCheckbox():
    def radio_checkbox_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        radio_button_female= driver.find_element(By.ID,"radio2")

        if radio_button_female.is_selected():
            pass
        else:
            radio_button_female.click()
            time.sleep(3)

        checkbox_blue =driver.find_element(By.ID,"checkbox2")

        if checkbox_blue.is_selected():
            pass
        else:
            checkbox_blue.click()
            time.sleep(3)

        driver.quit()


dsw = DemoRadioButtonAndCheckbox()
dsw.radio_checkbox_demo()