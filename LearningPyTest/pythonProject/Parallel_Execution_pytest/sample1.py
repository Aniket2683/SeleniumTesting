import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_omayo():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://omayo.blogspot.com")
    driver.maximize_window()
    time.sleep(2)


def test_selenium143():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://selenium143.blogspot.com/")
    driver.maximize_window()
    time.sleep(2)


def test_facebook():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://facebook.com/")
    driver.maximize_window()
    time.sleep(2)


def test_tutorialsninja():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    time.sleep(2)

# Above, if we run the test with pytest sample1.py then, all the test cases run sequentially.
# To run all the tests parallely, we installed package pytest-xdist. Now, we need to run the code with pytest -n number_of_testcases_that_you_want_to_exe_parallely
# eg . pytest -n 4  to run 4 test cases parallely or pytest sample1.py -n 4