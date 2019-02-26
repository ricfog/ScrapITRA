'''

scrape races

'''

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import os
import time
import csv



def get_races(browser, start_date, end_date, path=None):

    browser.get('https://itra.run/page/328/Results.html')
    WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'cal')))
    element = browser.find_element_by_xpath('//*[@id="periode"]/li[4]/label/input')
    browser.execute_script("arguments[0].click();", element)

    browser.implicitly_wait(20)


    # date

    start = browser.find_element_by_name("dtmin")
    start.clear()
    start.send_keys(start_date)
    start.send_keys(u'\ue007')

    time.sleep(4)

    end = browser.find_element_by_name("dtmax")
    end.clear()
    end.send_keys(end_date)
    time.sleep(2)
    end.send_keys(u'\ue007')

    time.sleep(4)

    store_race = []

    page_n = 0
    max_page = 1

    while page_n<max_page:

        store_page = []
        race_table = browser.find_element_by_id('cal')

        results = race_table.find_elements_by_css_selector("[onclick*='getResult']")
        time.sleep(4)

        race_info = race_table.find_elements_by_class_name('race')

        for it in range(len(results)):

            # click on the race
            info = race_info[it].text.split('\n')
            info[1] = info[1].replace(',','')
            store_page.append(info[:5])

            race = results[it]
            race.click()

            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'result')))

            # import with BeautifulSoup
            bs = BeautifulSoup(browser.page_source, 'lxml')
            table = bs.find('table', {'class':'palmares'})
            table_rows = table.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row = [tr.text.replace('\t', '').replace('\n', '').replace('\xa0','') for tr in td]
                store_page.append(row)

            browser.find_element_by_xpath('/html/body/div[4]/div[1]/a/span').click()


        browser.find_element_by_id('fdroite').click()
        store_race.append(store_page)

        time.sleep(10)
        max_page = int(float(browser.find_element_by_id('nbpmax').text))
        page_n += 1

    if path:
        with open(path, 'w') as f:
            writer_f = csv.writer(f)
            for item in store_race:
                writer_f.writerows(item)


    return store_race
