import imp
from optparse import Option
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from linkedinBot.scraperBot.scraper import login

# Creating a webdriver

chromeDriver_path = "E:\PythonVScode\DJANGO\linkedBot\chromedriver_win32\chromedriver.exe"
login_path = "https://linkedin.com/login"
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=chromeDriver_path, chrome_options=options)
driver.get(login_path)


# pass the username of the user
username = driver.find_element_by_id("username")
username.send_keys("abhi30september@gmail.com")


# pass the password for the same user
pword = driver.find_element_by_id("password")
pword.send_keys("@linkedin123@")


# click componant for the login into the account

driver.find_element_by_xpath("//button[@type='submit']").click()


profile_url = "https://www.linkedin.com/company/therapidhire/people/"
driver.get(profile_url) 


# search field

# searchField_xpath = '/html/body/div[6]/header/div/div/div/div[1]/input' 
# searchElement = driver.find_element_by_xpath(xpath=searchField_xpath)
# searchElement.click()
# time.sleep(2)
# searchElement.send_keys('the rapidhire')
# searchElement.send_keys(Keys.ENTER)




