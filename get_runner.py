'''
 get runners webapages
'''



import sys
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


def get_runner(first_name=None, last_name=None, nationality=None, browser=None):

    if browser:
        pass

    else:
        browser = webdriver.Chrome(executable_path='/Users/franco.fogliato/Desktop/chromedriver')
        browser.get('https://itra.run/community/')


    if first_name==None and last_name==None:
        sys.exit('At least one parameter needs to be specified!')

    else:

        if first_name:
            first_name_box = browser.find_element_by_xpath('//*[@id="searchRunner"]/div[1]/form/div[1]/input')
            first_name_box.send_keys(first_name)

        if last_name:
            last_name_box = browser.find_element_by_xpath('//*[@id="searchRunner"]/div[1]/form/div[2]/input')
            last_name_box.send_keys(last_name)

        if nationality:
            el = browser.find_element_by_id('nat')
            for option in el.find_elements_by_tag_name('option'):
                if option.text == nationality:
                    option.click()
                    break

    browser.find_element_by_xpath('//*[@id="searchRunner"]/div[1]/form/a').click()
    #WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'run2704')))
    WebDriverWait(browser, 100).until(EC.visibility_of_element_located((By.ID, 'searchRes')))

    #element = browser.find_element_by_id('searchRes')
    #browser.execute_script("arguments[0].setAttribute('style','visibility:visible;');",element)

    elements = browser.find_element_by_id('searchRes').find_elements_by_class_name('fc')

    #elements = browser.find_elements_by_class_name('fc')
    l = []
    for element in elements:
        l.append(element.get_attribute('data-url'))

    return l


if __name__=='__main__':
    #get_runner('Riccardo', 'Fogliato', 'Italy')
    get_runner('a', nationality='Italy')
    #get_runner('oroafsdfsd', 'dsadsa', 'sda')
