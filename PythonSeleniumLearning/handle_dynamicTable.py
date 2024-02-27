from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DyamicTable_demo():
    def handle_dynamicTable(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.opencart.com/admin/")
        driver.maximize_window()
        driver.find_element(By.ID,"input-username").send_keys("demo")
        driver.find_element(By.ID,"input-password").send_keys("demo")
        driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
        # driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        time.sleep(2)

        if not (driver.title.__eq__("Dashboard")):
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Widget containing a Cloudflare security challenge']")))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='ctp-checkbox-label']"))).click()

        driver.implicitly_wait(20)
        driver.find_element(By.CLASS_NAME,"btn-close").click()
        driver.find_element(By.XPATH,"//a[contains(text(),'Sales')]").click()
        driver.find_element(By.XPATH,"//a[contains(text(),'Orders')]").click()
        time.sleep(4)

        expected_name = "Arun Kumar"
        # extracting all the names from Customer column in the table
        customer_names = driver.find_elements(By.XPATH,"//form[@id ='form-order' ]//tr/td[4]")
        i=1
        for names in customer_names:
            if names.__eq__(expected_name):
        #         creating a dynamic xpath for that particular cell to check the checkbox
                xpath_text = "//form[@id ='form-order' ]//tr//td[text()='"+expected_name+"']"
                driver.find_element(By.XPATH,xpath_text).click()
            i=i+1
        time.sleep(5)
        driver.quit()

demo1 = DyamicTable_demo()
demo1.handle_dynamicTable()