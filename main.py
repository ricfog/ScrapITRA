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

from get_runner import *
from scrap_record import *
from login import *
#from scrap_perf import *
from retrieve_nat import *

 # locate browser
dir_path = os.path.dirname(os.path.realpath(__file__))
path_driver = os.path.join(dir_path,'chromedriver')
 # going healess
#options = Options()
#options.headless = True
#browser = webdriver.Chrome(executable_path=path_driver, chrome_options=options)
#browser = webdriver.Chrome(executable_path='/Users/franco.fogliato/Desktop/chromedriver', chrome_options=options)
 # visible browser
browser = webdriver.Chrome(executable_path=path_driver)


 # initialize on the webpage
main_webpage = 'https://itra.run/community/'
browser.get(main_webpage)

 # identification of the user -> access to more information but needs membership
login('ricfogliato', 'D89MM286', browser)

 # retrieve list of available nationalities
nationality_list = retrieve_nat(main_webpage, browser)


''' scraping sequentially '''

#webpage_list = get_runner(first_name='dfds', last_name='dsfsdf', nationality = 'Italy', browser=browser)

# iterate in alphabetical order
letters = list(string.ascii_lowercase)
#letters.extend([i+b for i in letters for b in letters])
#letters = letters[26:]
letters_extended = cp.copy(letters)
letters_extended.extend([i+b for i in letters for b in letters])
letters_extended = letters_extended[26:]


with open('performance.csv', 'w') as p, open('record.csv', 'w') as r:
    writer_p = csv.writer(p)
    writer_r = csv.writer(r)

    #for nat in nationality_list:
    for first_in in letters:
        for last_in in letters_extended:
            print(first_in, last_in)
            browser.get(main_webpage)
           # webpage_list = get_runner(first_name = first_in, last_name = last_in, nationality = nat, browser = browser)
            webpage_list = get_runner(first_name = first_in, last_name = last_in, browser = browser)
            if webpage_list:
                for webpage in webpage_list:
                    record, performance = scrape_history(webpage, browser)
                    writer_p.writerows(performance)
                    writer_r.writerows(record)


browser.quit()
