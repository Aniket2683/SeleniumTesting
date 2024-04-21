import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities import readConfig


@pytest.fixture(scope="function")
def driver():
    driver = None
    browser = readConfig.read_config("basic info","browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

    url = readConfig.read_config("basic info","url")
    driver.get(url)
    yield driver
    driver.quit()
