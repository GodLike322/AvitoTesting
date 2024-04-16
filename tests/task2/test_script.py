from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver_login = webdriver.Chrome()

driver_login.get("https://www.avito.ru/avito-care/eco-impact#login?next=authCallbackEcoImpact")
time.sleep(2)

driver_login.maximize_window()

input_number = driver_login.find_elements(By.TAG_NAME, 'input')
input_number[0].send_keys("...")
time.sleep(5)

input_pass = driver_login.find_elements(By.TAG_NAME, 'input')
input_pass[1].send_keys("...")
time.sleep(5)

btn_login = driver_login.find_elements(By.TAG_NAME, 'button')
btn_login[9].click()
time.sleep(30)

driver_login.execute_script("window.scrollBy(0, 800);")

driver_login.save_screenshot('...')

driver_login.quit()

