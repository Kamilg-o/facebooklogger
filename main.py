from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)



# launching the webdriver
driver = webdriver.Chrome(chrome_options=chrome_options)

# website launch
driver.get("http://www.facebook.com")

time.sleep(2)

# bypassing the acceptance of cookies
cookie_button = driver.find_element_by_xpath("//button[text()='Akceptuj wszystkie']")
cookie_button.click()

# log in
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

username.clear()
username.send_keys('username')
password.clear()
password.send_keys('password')

time.sleep(3)

login_button = driver.find_element_by_xpath("//button[text()='Zaloguj się']")
login_button.click()

time.sleep(2)

