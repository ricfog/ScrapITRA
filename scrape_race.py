from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import string
import csv
import os
import copy as cp

from login import *


 # locate browser
dir_path = os.path.dirname(os.path.realpath(__file__))
path_driver = os.path.join(dir_path,'chromedriver')
 # going healess
options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path=path_driver, chrome_options=options)
#browser = webdriver.Chrome(executable_path='/Users/franco.fogliato/Desktop/chromedriver', chrome_options=options)
 # visible browser
#browser = webdriver.Chrome(executable_path=path_driver)

browser.implicitly_wait(20)

 # initialize on the webpage
main_webpage = 'https://itra.run/community'
browser.get(main_webpage)

 # identification of the user -> access to more information but needs membership
#login('ricfogliato', 'D89MM286', browser)

browser.get('https://itra.run/page/328/Results.html')
WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'cal')))

element = browser.find_element_by_xpath('//*[@id="periode"]/li[4]/label/input')
browser.execute_script("arguments[0].click();", element)

#time.sleep(2)
#WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, '')))
start = browser.find_element_by_name("dtmin")
start.clear()
start.send_keys('01/01/2010')

time.sleep(6)

with open('races', 'w') as r:
    writer_r = csv.writer(r)
    page_n = 0
    max_page = 1
    while page_n<max_page:
        print(page_n)
        store = []
        race_table = browser.find_element_by_id('cal')
        #browser.find_element_by_xpath('//*[@id="cal"]/div[2]/a').click()
        n_el = len(race_table.find_elements_by_css_selector("[onclick*='getResult']"))
        #for race in  race_table.find_elements_by_css_selector("[onclick*='getResult']"):
        for it in range(n_el):
            info = race_table.find_elements_by_class_name('race')[it].text.split('\n')
            info[1] = info[1].replace(",", "")
            store.append(info[:5])
            #info = info.split('\n'))
            # store.append(info.text[:5])
            race = race_table.find_elements_by_css_selector("[onclick*='getResult']")[it]
            #element = race.find_element_by_tag_name('h2')
            race.send_keys("\n")
            #WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'result')))
            #results = browser.find_element_by_id('result')
            #bs = BeautifulSoup(results.get_attribute('innerHTML'), 'lxml')
            time.sleep(10)
            bs = BeautifulSoup(browser.page_source, 'lxml')
            table = bs.find('table', {'class':'palmares'})
            table_rows = table.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row = [tr.text.replace('\t', '').replace('\n', '').replace('\xa0','') for tr in td]
                store.append(row)
            #time.sleep(15)
            writer_r.writerows(store)
            browser.find_element_by_xpath('/html/body/div[4]/div[1]/a/span').click()
            #time.sleep(10)
            #print(BeautifulSoup(browser.page_source, 'lxml'))
        browser.find_element_by_id('fdroite').click()
        max_page = int(float(browser.find_element_by_id('nbpmax').text))
        page_n += 1

browser.quit()
