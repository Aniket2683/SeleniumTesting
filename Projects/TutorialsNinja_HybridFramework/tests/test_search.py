import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_search_for_a_valid_product(driver):
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()  # Clear any existing input
    search_input.send_keys("HP")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    time.sleep(2)


def test_search_for_an_invalid_product(driver):
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()  # Clear any existing input
    search_input.send_keys("Honda")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text == expected_text
    time.sleep(2)


def test_search_without_providing_any_product(driver):
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()  # Clear any existing input
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text == expected_text
    allure.attach(driver.get_screenshot_as_png(), name="search_without_providing_any_product",attachment_type=AttachmentType.PNG)
    time.sleep(2)
