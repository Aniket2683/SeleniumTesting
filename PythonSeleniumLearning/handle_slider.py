import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class Demo_slider():
    def slider_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/p/page3.html")
        driver.maximize_window()
        min_slider = driver.find_element(By.XPATH,"//a[@aria-labelledby='price-min-label']")
        action = ActionChains(driver)
        action.move_to_element(min_slider).drag_and_drop_by_offset(min_slider,-100,0).perform()
        time.sleep(3)

        driver.quit()


dsw = Demo_slider()
dsw.slider_demo()