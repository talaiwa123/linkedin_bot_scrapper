# from linkedin_auto_connect_bot import *

# login_status = linkedin.login(username="upayanvyas22@gmail.com",password="uvuv1234")
# print("login_status: ", login_status)

# linkedin.send_connection(profile_link='profile_link')
# people_results = linkedin.people_results()
# print("people_results: ", people_results)
# search_jobs = linkedin.search_jobs(keyword='python developer')
# print("search_jobs: ", search_jobs)

# from os import environ as env
# from os import environ as env
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


chromeDriver_path = "E:\PythonVScode\DJANGO\linkedBot\chromedriver_win32\chromedriver.exe"
web_url = 'https://www.linkedin.com/home'

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(
    executable_path=chromeDriver_path, chrome_options=options)


def myNetwork(myNetwork_xpath):
    # click connections menu on nav bar
    try:
        print("Opening Networks tab using xpath...")
        myNetwork_el = driver.find_element_by_xpath(xpath=myNetwork_xpath)
        print("myNetwork_el: ", myNetwork_el)
        myNetwork_el.click()
    except:
        print('Some error occured, now trying to open networks tab directly...')
        print(driver.get('https://www.linkedin.com/mynetwork/'))

    
    # people = '/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[1]/ul'
    # people_el = driver.find_element_by_xpath(xpath=people)
    # print("people_el: ", people_el)

    # # Click on see all People
    # see_all_xpath = '/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[1]/div/button'
    # see_all_el = driver.find_element_by_xpath(xpath=see_all_xpath)
    # print('see_all_el: ', see_all_el)

# # search company name
def search():
    searchField_xpath = '/html/body/div[6]/header/div/div/div/div[1]/input' 
    searchElement = driver.find_element_by_xpath(xpath=searchField_xpath)
    searchElement.click()
    time.sleep(2)
    searchElement.send_keys('therapidhire')
    searchElement.send_keys(Keys.ENTER)

    myNetwork('/html/body/div[6]/header/div/nav/ul/li[2]/a')


def login(username, password):
    email_xpath = '/html/body/div/main/div[2]/div[1]/form/div[1]/input'
    password_xpath = '/html/body/div/main/div[2]/div[1]/form/div[2]/input'
    login_button_xpath = '/html/body/div/main/div[2]/div[1]/form/div[3]/button'

    email_el = driver.find_element_by_xpath(xpath=email_xpath)
    print("email_el: ", email_el)
    email_el.send_keys(username)

    password_el = driver.find_element_by_xpath(xpath=password_xpath)
    print("password_el: ", password_el)
    password_el.send_keys(password)

    login_button_el = driver.find_element_by_xpath(xpath=login_button_xpath)
    print("login_button_el: ", login_button_el)
    login_button_el.click()

    search()

# # Go to My Networks Page
    # myNetwork('/html/body/div[6]/header/div/nav/ul/li[2]/a')




def main():
    login_url = 'https://www.linkedin.com/login'
    driver.get(login_url)
    time.sleep(3)
    login(username='abhi30september@gmail.com', password='@linkedin123@')


if __name__ == '__main__':
    main()