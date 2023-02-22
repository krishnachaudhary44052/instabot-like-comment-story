
# Instagram Like Comment Bot

It automatically logs on to Instagram with the provided email and password and searches for the account mentioned and open the posts and stories of the mentioned details and it Like and comment randomly provided in the list for the ten posts.
Note: It do not unlike the post which is already liked.
Setup:




# Instagram Like Comment Bot

It automatically logs on to Instagram with the provided email and password and searches for the account mentioned and open the posts of the mentioned details and it Like and comment randomly provided in the list for the ten posts. Note: It do not unlike the post which is already liked.

## Installation
1.Clone this repo to your local machine.

2.Create a virtual environment using the following commands.



```
  python3 -m venv env # Run this command in your terminal for creating virtual enviroment
   source env\scripts\activate # after creating virtual enviroment you have to activate it 
```
3.Install the selenium
```
   pip install selenium
```
4.Install chrome driver.
```
   pip install chromedrivermanager
```
5.Check the version of your browser and DOWNLOAD the chrome driver of the same version.

6.Unzip the downloaded file and copy the location of your web driver.
```
   Location may look like on windows.
   C:\Users\devch\OneDrive\Desktop\sele
```
7.Add the Instagram url to the driver path.
```
   Look like.
   "https://www.instagram.com/accounts/login/"
   
```
8.In the insta.py file make sure to enter the necessary information like
```
   #Your insta email
     email = " "
   #Your insta password
     password = " "
   
```
## Note:
1. Note
If you are on mac and if you are running this code make sure to go to System Preferences> Security and Privacy and allow Chrome web driver to run.
2. Note
a. If  you are using Insta bot u have to implement sleep time for every steps for avoiding instagram bot detection.
b. Make sure your login and logout limit will be not more than 10 times a day.
c. The sleep time should be more than 10 sec for look like a normal human.
d. Dont pass the 

## Documentation:
```
  from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sha512_crypt
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)
username = driver.find_element(by=By.NAME,value="username")
password = driver.find_element(by=By.NAME,value="password")

username.send_keys("extern_insta")
password.send_keys("extern123")
time.sleep(5)
driver.find_element(by=By.XPATH,value="/html/body").click()
# driver.find_element('xpath', '/html/body').click()
time.sleep(4)

driver.maximize_window() # For maximizing window
driver.implicitly_wait(5)
driver.find_element(by=By.XPATH,value='//button[contains(text(), "Not Now")]').click()
time.sleep(5)
driver.find_element(by=By.XPATH,value='//button[contains(text(), "Not Now")]').click()
time.sleep(5)
search_box = driver.get("https://www.instagram.com/explore/tags/naturelovers/")
time.sleep(4)
comments = ["Awesome!","Love it!","Looks great!","So cool!","Incredible!","Amazing!","Fantastic!","Beautiful!","Spectacular!","Stunning!"]
posts = driver.find_elements(by=By.XPATH, value="//a[contains(@href,'/p/')]")
for i in range(10):
    posts[i].click()
    time.sleep(5)
    driver.find_element(by=By.XPATH, value="//button/div/*[*[local-name()='svg']/@aria-label='Like']/*").click()
    
    time.sleep(5)
    driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']").click()
    
    time.sleep(5)
    comment_field = driver.find_element(by=By.XPATH, value="//textarea[@placeholder='Add a comment…']")
    comment_field.send_keys(random.choices(comments))
    comment_field.send_keys(Keys.RETURN)
   
    # Wait for the comment to post
    time.sleep(3)
    # Go back to the hashtag page
    driver.back()
    # Wait for the page to load
    time.sleep(3)
# Close the driver

driver.quit()
   

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

