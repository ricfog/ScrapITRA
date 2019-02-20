'''

Scrape runners from provided list

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
path_driver = os.path.join(dir_path,'Drivers/firefox_mac')
browser = webdriver.Firefox(options=options, executable_path=path_driver)


 # initialize on the webpage
 main_webpage = 'https://itra.run/community/'
 browser.get(main_webpage)


 # login
 def login_account():
     try:
        from login_credentials import *
        login(username, password, browser)
     except ImportError:
        pass

login_account()



with open('Files/selected_runners.csv', 'r') as f:
    reader = csv.reader(f)
    sel_runner = list(reader)


with open('performance.csv', 'w') as p, open('record.csv', 'w') as r:
    writer_p = csv.writer(p)
    writer_r = csv.writer(r)

    # monitoring process
    progress = 0
    total_work = len(sel_runner)
    milestone = total_work*0.01/100

    for runner in sel_runner:

        # print progress
        progress += 1/total_work
        if progress >= milestone:
            print('Progress of the work is currently at ', progress/total_work, '%')
            milestone += total_work*0.01/100

        # check connection is not expired
        try:
            find_elements_by_xpath("//*[contains(text(), 'Connect / Create an account')]")
            login_account()
        except:
            pass

        browser.get(main_webpage)
        webpage_list = get_runner(browser = browser, first_name = runner[0], last_name = runner[1])
        if webpage_list:
            for webpage in webpage_list:
                record, performance = scrape_history(webpage, browser)
                writer_p.writerows(performance)
                writer_r.writerows(record)
