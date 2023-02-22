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
time.sleep(5)

# name of account you want to search
hashtag_list = 'mobileapp'
driver.get(f'https://www.instagram.com/explore/tags/{hashtag_list}')
logging.info(f'Exploring #{hashtag_list}')
time.sleep(4)

# here you have to give the comments you want to add on the post
comments1 = ["I like your work!, we do something similler as well. visit our main profile. link in my bio",]
posts = driver.find_elements(by=By.XPATH, value="//a[contains(@href,'/p/')]")

#No of posts you wants to like or comment
No_posts = 10
for i in range(No_posts):
    posts[i].click()
    time.sleep(5)
    driver.find_element(by=By.XPATH, value="//button/div/*[*[local-name()='svg']/@aria-label='Like']/*").click()
    time.sleep(5)
    driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").click()
    time.sleep(5)
    comment_field = driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']")
    comment_field.send_keys(random.choices(comments1))
    comment_field.send_keys(Keys.RETURN)
    # Wait for the comment to post
    time.sleep(3)
    # Go back to the hashtag page
    driver.back()
    # Wait for the page to load
    time.sleep(3)
    
# Close the driver

driver.quit()



