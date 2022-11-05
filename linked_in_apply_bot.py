from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = 'https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F%3Ftrk%3Dnav_logo&fromSignIn=true&trk=cold_join_sign_in'
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)
time.sleep(2)

# log in boxes
email_username = driver.find_element(By.ID, 'username')
password_box = driver.find_element(By.ID, 'password')
# email
email_username.send_keys('biz.aolney@gmail.com')
# password
with open('linkedin_creds.txt', 'r') as PASSWORD:
    password_box.send_keys(PASSWORD.read())
time.sleep(1)
button = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]')
button.click()
time.sleep(2)
search = driver.find_element(By.CLASS_NAME, 'jobs-search-box__text-input')
search.send_keys('jr python developer')
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jobs-search-box-location-id-ember610"]'))).send_keys('Portland')


