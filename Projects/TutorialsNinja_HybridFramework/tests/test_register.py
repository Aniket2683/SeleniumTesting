from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pytest

def generate_email_timestamp():
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    timestamp = timestamp.replace('-', '_').replace(' ', '_').replace(':', '_')
    return "aniket" + timestamp + "@gmail.com"

def test_create_account_with_mandatory_fields(driver):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "input-firstname").send_keys("Aniket")
    time.sleep(1)
    driver.find_element(By.ID, "input-lastname").send_keys("Jaiswal")
    time.sleep(1)
    # once to run the script, you will need to update the email as you cannot register with an already registered email.
    # here we use email with a timestamp
    driver.find_element(By.ID, "input-email").send_keys(generate_email_timestamp())
    driver.find_element(By.ID, "input-telephone").send_keys("1245365478")
    driver.find_element(By.ID, "input-password").send_keys("121212")
    driver.find_element(By.ID, "input-confirm").send_keys("121212")
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    time.sleep(1)
    expected_text = "Your Account Has Been Created!"
    assert driver.find_element(By.XPATH, "//div[@id='content']/h1").text == expected_text

def test_create_account_with_all_required_fields(driver):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "input-firstname").send_keys("Aniket")
    time.sleep(1)
    driver.find_element(By.ID, "input-lastname").send_keys("Jaiswal")
    time.sleep(1)
    # once to run the script, you will need to update the email as you cannot register with an already registered email.
    # here we use email with a timestamp
    driver.find_element(By.ID, "input-email").send_keys(generate_email_timestamp())
    driver.find_element(By.ID, "input-telephone").send_keys("1245365478")
    driver.find_element(By.ID, "input-password").send_keys("121212")
    driver.find_element(By.ID, "input-confirm").send_keys("121212")
    driver.find_element(By.XPATH, "//input[@value='1'][@name='newsletter']").click()
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    time.sleep(1)
    expected_text = "Your Account Has Been Created!"
    assert driver.find_element(By.XPATH, "//div[@id='content']/h1").text == expected_text
