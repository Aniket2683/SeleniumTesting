import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_omayo():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    expected_title = "Your Store ABC"
    actual_title = driver.title
    assert actual_title.__eq__(expected_title)

    driver.find_element(By.NAME,"search").send_keys("HP")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    time.sleep(2)
    driver.quit()

# use flag --soft-asserts  for soft assertion