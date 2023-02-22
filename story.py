from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sha512_crypt
from selenium.webdriver.common.by import By
import logging

driver = webdriver.Chrome()
# path for instagram
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)
username = driver.find_element(by=By.NAME,value="username")
password = driver.find_element(by=By.NAME,value="password")

# You have to provide the username 
username.send_keys("extern_insta")
# You have to provide the password
password.send_keys("extern123")
time.sleep(5)
driver.find_element(by=By.XPATH,value="/html/body").click()
# driver.find_element('xpath', '/html/body').click()
time.sleep(4)
# For maximizing window
driver.maximize_window() 
driver.implicitly_wait(5)
driver.find_element(by=By.XPATH,value='//button[contains(text(), "Not Now")]').click()
time.sleep(5)
driver.find_element(by=By.XPATH,value='//button[contains(text(), "Not Now")]').click()
time.sleep(10)
driver.find_element(by=By.XPATH,value='''//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd'][@href='#']
''').click()
time.sleep(5)
driver.find_element(by=By.XPATH, value="//input[@aria-label='Search input']").click()
# input the name of user account 

comments = 'galaxycarsdelhi'   
time.sleep(5)
search_field = driver.find_element(by=By.XPATH, value="//input[@aria-label='Search input']")
search_field.send_keys(comments)
search_field.send_keys(Keys.RETURN)
time.sleep(5)

driver.get(f'https://www.instagram.com/{comments}/')
time.sleep(5)
try:
    driver.find_element(by=By.XPATH,value="//div[contains(@class,'_aarf')]/canvas[@class='_aarh']//following-sibling::span/img").click()
    time.sleep(10)
except:
    driver.back()
driver.quit()

