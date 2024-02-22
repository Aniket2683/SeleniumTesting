from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Demo_calendar1():
    def calendar1_demo(self,month,year,date):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
        driver.find_element(By.ID,"datepicker").click()
        wait = WebDriverWait(driver,4)
        wait.until(expected_conditions.presence_of_element_located((By.ID,"ui-datepicker-div")))
        time.sleep(3)

        current_month = driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text
        current_year = driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text

        while not (current_month.__eq__(month) and current_year.__eq__(year)):
            # click on next button
            driver.find_element(By.XPATH,"//span[text()='Next']").click()
            # update the current month and year
            current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
            current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

        #now click on date
        date_Xpath = "//td[@data-handler='selectDay']/a[text()='"+date+"']"
        driver.find_element(By.XPATH,date_Xpath).click()
        time.sleep(3)

        driver.quit()

demo1= Demo_calendar1()
demo1.calendar1_demo("August","2024","26")
