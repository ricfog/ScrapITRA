'''

Scrape individual track record

@author: rfogliat@andrew.cmu.edu

'''


from import_modules import *



def scrape_history(webpage, browser):

    browser.get('https://itra.run'+webpage)

    # to handle mistakes in ITRA website
    try:
        browser.find_element_by_xpath('//*[@id="searchRunner"]/div[1]/form/a')
        return ([],[])
    except:
        pass



    # scrape list of runners
    browser.find_element_by_link_text('Results').click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'tabpalm')))


    
    # import and process in BeautifulSoup
    bs = BeautifulSoup(browser.page_source, 'lxml')

    
    # scrape record
    table = bs.find('table', {'id':'tabpalm'})
    table_rows = table.find_all('tr')
    record = []
    for tr in table_rows[1:]:
        td = tr.find_all('td')
        row = [tr.text.replace('\t', '').replace('\n', '').replace('\xa0','') for tr in td]
        if row[0][-1] != '-':
            row.insert(0, '')
        row.insert(0,webpage)
        record.append(row[0:8])

        
    # scrape performance
    table = bs.find("tbody", {"id": "tabraceip"})
    table_rows = table.find_all('tr')
    performance = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text.replace('\t', '').replace('\n', '').replace('\xa0','') for tr in td]
        if row[0][-1] != '-':
            row.insert(0, '')
        row[0] = webpage
        performance.append(row[0:9])

        
    return (record, performance)


