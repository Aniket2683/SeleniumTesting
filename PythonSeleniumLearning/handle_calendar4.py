import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class handle_calendar4():
    def demo_calendar4(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")
        driver.maximize_window()
        driver.find_element(By.ID,"fourth_date_picker").click()

        wait = WebDriverWait(driver,10)
        wait.until(expected_conditions.visibility_of_element_located((By.ID,"ui-datepicker-div")))

        dropdown_month = driver.find_element(By.CLASS_NAME,"ui-datepicker-month")
        select_month = Select(dropdown_month)
        select_month.select_by_visible_text("Aug")

        dropdown_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
        select_year = Select(dropdown_year)
        select_year.select_by_visible_text("2024")

        driver.find_element(By.XPATH,"//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='26']").click()
        time.sleep(5)
        driver.quit()

demo1 = handle_calendar4()
demo1.demo_calendar4()