from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class handle_table_heading_demo():
    def table_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()

        table_headings = driver.find_elements(By.XPATH,"//table[@id='table1']//th")

        for headings in table_headings:
            print(headings.text)

        driver.quit()
demo1 = handle_table_heading_demo()
demo1.table_demo()


