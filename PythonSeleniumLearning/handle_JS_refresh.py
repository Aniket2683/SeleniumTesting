from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Demo_JS_Refresh():
    def handle_JSrefresh(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        time.sleep(3)
        # JS way is a bit faster than selenium.
        # Note : It is for education purpose ,in real-time  we use Selenium way only.
        # In some rare cases if, Selenium way fails, we can use JS way
        driver.execute_script("location.reload()")
        time.sleep(4)


        driver.quit()

demo1 = Demo_JS_Refresh()
demo1.handle_JSrefresh()