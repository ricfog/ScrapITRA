'''

Scrape all races from ITRA website

TODO: fixed once conneciton to Hydra is restored
'''


from import_modules import *


# get browser
options = Options()
options.headless = False # go headless
dir_path = os.path.dirname(os.path.realpath(__file__))
path_driver = os.path.join(dir_path,'firefox_mac')
browser = webdriver.Firefox(options=options, executable_path=path_driver)


# initialize browser
main_webpage = 'https://itra.run/community'
browser.get(main_webpage)


browser.get('https://itra.run/page/328/Results.html')
WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'cal')))
element = browser.find_element_by_xpath('//*[@id="periode"]/li[4]/label/input')
browser.execute_script("arguments[0].click();", element)


start = browser.find_element_by_name("dtmin")
start.clear()
start.send_keys('10/05/2018')
end = browser.find_element_by_name("dtmax")
end.clear()
end.send_keys('20/01/2019')
time.sleep(6)


with open('races', 'w') as r:

    writer_r = csv.writer(r)
    page_n = 0
    max_page = 1

    time.sleep(10)

    while page_n<max_page:

        store = []
        race_table = browser.find_element_by_id('cal')

        n_el = len(race_table.find_elements_by_css_selector("[onclick*='getResult']"))


        for it in range(n_el):


            # click on the race
            info = race_table.find_elements_by_class_name('race')[it].text.split('\n')
            info[1] = info[1].replace(',','')
            store.append(info[:5])
            race = race_table.find_elements_by_css_selector("[onclick*='getResult']")[it]
            race.send_keys("\n")

            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'result')))

            # import with BeautifulSoup
            bs = BeautifulSoup(browser.page_source, 'lxml')
            table = bs.find('table', {'class':'palmares'})
            table_rows = table.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row = [tr.text.replace('\t', '').replace('\n', '').replace('\xa0','') for tr in td]
                store.append(row)

            writer_r.writerows(store)
            browser.find_element_by_xpath('/html/body/div[4]/div[1]/a/span').click()
            browser.find_element_by_id('fdroite').click()

        time.sleep(10)
        max_page = int(float(browser.find_element_by_id('nbpmax').text))
        page_n += 1

browser.quit()
