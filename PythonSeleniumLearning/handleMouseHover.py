import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class Demo_hoverMouse():
    def hover_mouse_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        Blogs = driver.find_element(By.ID,"blogsmenu")

        action = ActionChains(driver)
        action.move_to_element(Blogs).perform()
        time.sleep(3)
        sele_143 = driver.find_element(By.XPATH,"//a/span[text()='Selenium143']")
        action.move_to_element(sele_143).click().perform()
        time.sleep(3)

        driver.quit()


dsw = Demo_hoverMouse()
dsw.hover_mouse_demo()