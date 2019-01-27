'''
 scrap individual track record
'''


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def scrap_record(webpage, browser=None):

    if browser:
        pass
    else:
        browser = webdriver.Chrome(executable_path='/Users/franco.fogliato/Desktop/chromedriver')

    browser.get('https://itra.run'+webpage)

    browser.find_element_by_link_text('Results').click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'tabpalm')))

    bs = BeautifulSoup(browser.page_source, 'lxml')

    table = bs.find('table', {'id':'tabpalm'})
    table_rows = table.find_all('tr')
    l = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text.replace('\t', '').replace('\n', '').replace('\xa0','') for tr in td]
        if row[0][-1] != '-':
            row.insert(0, '')
        l.append(row[0:7])
    return l



if __name__=='__main__':
    scrap_record('/community/kilian.jornet%20burgada/2704/9736/')
