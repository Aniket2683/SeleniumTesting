import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://monkeytype.com/")
try:
    driver.find_element(By.XPATH, "//button[text() = 'accept all']").click()
except NoSuchElementException:
    pass
time.sleep(1)

while True:
    word_elements = driver.find_elements(By.XPATH, "//*[@id='words']/div")

    # Find the index of the active word
    activeIndex = None
    for i, word_element in enumerate(word_elements):
        if 'active' in word_element.get_attribute("class"):
            activeIndex = i
            break

    if activeIndex is not None:
        word_elements = word_elements[activeIndex:]
        for word_element in word_elements:
            letters = ""
            while True:
                try:
                    letter_elements = word_element.find_elements(By.XPATH, ".//letter")
                    for letter_element in letter_elements:
                        letters += letter_element.text
                    letters += " "
                    ActionChains(driver).send_keys(letters).perform()
                    break
                except StaleElementReferenceException:
                    # Re-find the word element
                    word_elements = driver.find_elements(By.XPATH, "//*[@id='words']/div")
                    if activeIndex < len(word_elements):
                        word_elements = word_elements[activeIndex:]
                    else:
                        # If activeIndex is out of range, break out of the loop
                        break
    else:
        # If no active word is found, wait for a brief moment before trying again
        time.sleep(0.5)
        driver.quit()



