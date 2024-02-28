from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Demo_JS_Title():
    def handle_JSTitle(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://omayo.blogspot.com/")
        driver.maximize_window()
        # JS way is a bit faster than selenium.
        # internally selenium's 'driver.title' also uses JS only.
        # Note : return keyword is important. Otherwise, it will print None.
        # Note : It is for education purpose ,in real-time  we use Selenium way only.
        print(str(driver.execute_script("return document.title")))



        driver.quit()

demo1 = Demo_JS_Title()
demo1.handle_JSTitle()