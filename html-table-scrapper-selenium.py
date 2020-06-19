from selenium import webdriver
import time
import csv
import pandas as pd
class TableScrapper:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        file_header = []
        file_body = []

        time.sleep(4)  #give time to fully load the page

        table = driver.find_element_by_id("table_id")
        head = table.find_element_by_tag_name('thead')
        head_line = head.find_element_by_tag_name('tr')
        headers = head_line.find_elements_by_tag_name('th')
        for header in headers:
            header_text = header.text
            file_header.append(header_text)
        file_body.append(file_header)

        csvfile = open('csvfilename.csv', 'w', newline='')
        wr = csv.writer(csvfile)

        for row in table.find_elements_by_css_selector('tr'):
            x = [d.text for d in row.find_elements_by_css_selector('th')]
            if len(x):
                wr.writerow(x)
                break
        
        while True:
            '''
            Put Break Conditions accordingly
            '''
            row_elem_cnt = 0
            for row in table.find_elements_by_css_selector('tr'):
                row_elem_cnt += 1
                x = [d.text for d in row.find_elements_by_css_selector('td')]
                if len(x):
                    wr.writerow(x) #Write tha rowdata into a csv file
            driver.find_element_by_id('next_button_id').click() #Change the id of next button
            time.sleep(4) #give time to fully load the page
            table = driver.find_element_by_id("table_id") #table id that you want to scrap
            
        driver.quit()
if __name__ == '__main__':
    url = '' #give your url to scrap
    scrap = TableScrapper(url)
    scrap.scrap()
