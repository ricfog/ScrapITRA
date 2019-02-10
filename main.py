'''

Main file with custom functions

@author: rfogliat@andrew.cmu.edu


'''



#  import all modules from package
from import_modules import *


# import functions from other modules
from login import *
from get_runner import *
from scrape_history import *


#  get browser 
options = Options()
options.headless = True # go headless
dir_path = os.path.dirname(os.path.realpath(__file__))
path_driver = os.path.join(dir_path,'firefox_mac')
browser = webdriver.Firefox(options=options, executable_path=path_driver)


# initialize on the webpage
main_webpage = 'https://itra.run/community/'
browser.get(main_webpage)


# login
try:
   from login_credentials import *
   login(username, password, browser)
except ImportError:
   pass



# scrape runner
with open('performance.csv', 'w') as p, open('record.csv', 'w') as r:
    writer_p = csv.writer(p)
    writer_r = csv.writer(r)

    first_in = 'Riccardo'
    last_in = 'Fogliato'
    webpage_list = get_runner(browser=browser, first_name=first_in, last_name=last_in)
    if webpage_list:
        for webpage in webpage_list:
            record, performance = scrape_history(webpage, browser)
            writer_p.writerows(performance)
            writer_r.writerows(record)


browser.quit()
