'''
 retrieve nationalities available
'''


import sys
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


def retrieve_nat(webpage, browser=None):


    if browser:
        pass

    else:
        browser = webdriver.Chrome(executable_path='/Users/franco.fogliato/Desktop/chromedriver')
        browser.get(webpage)


    el = browser.find_element_by_id('nat')
    l = []
    for option in el.find_elements_by_tag_name('option')[1:]:
        l.append(option.text)

    return(l)


if __name__=='__main__':
    retrieve_nat('https://itra.run/community/')
