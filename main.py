from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

# launching the webdriver
driver = webdriver.Chrome()

# website launch
driver.get("http://www.facebook.com")

time.sleep(2)

# bypassing the acceptance of cookies
cookie_button = driver.find_element_by_xpath("//button[text()='Akceptuj wszystkie']")
cookie_button.click()
