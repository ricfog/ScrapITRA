'''
 logging in for ITRA website
 needs membership
'''

import sys
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


def login(username, password, browser=None):

    if browser:
        pass
    else:
        browser = webdriver.Chrome(executable_path='/Users/franco.fogliato/Desktop/chromedriver')
        browser.get('https://itra.run/community')

    browser.find_element_by_class_name('btnconnect').click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn')))

    user_box = browser.find_element_by_xpath('//*[@id="fMemb"]/input[1]')
    user_box.send_keys(username)

    password_box = browser.find_element_by_xpath('//*[@id="fMemb"]/input[2]')
    password_box.send_keys(password)


    browser.find_element_by_class_name('btn').click()




if __name__=='__main__':
    login('ricfogliato', 'D89MM286')
