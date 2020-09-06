from selenium import webdriver
import time
import csv
import pandas as pd
class Scrapper:
    def __init__(self):
        
        self.SEARCH_URL_1 = "https://www.amazon.de/s?i=merchant-items&me=A3SIK4R9XSGRE7&page="
        self.SEARCH_URL_2 = "&marketplaceID=A1PA6795UKMFR9&qid=1595144474&ref=sr_pg_"

    def get_asin(self, url_link):
        asin = ''
        elems = url_link.split('/')
        for i in range(len(elems)):
            if elems[i] == 'dp' and i + 1 < len(elems):
                asin = elems[i + 1]
                break
        return asin

    def scrap(self, start, end):
        driver = webdriver.Chrome()
        f = open('asin.txt', 'w+')
        asin_code = set()
        while start <= end:
            url =  url = self.SEARCH_URL_1 + str(start) + self.SEARCH_URL_2 + str(start)
            driver.get(url)
            time.sleep(2)  #give time to fully load the page
            data_arr = driver.find_elements_by_css_selector(".a-link-normal.a-text-normal")

            print('Page No', start, 'Total Data len', len(data_arr))
            for data in data_arr:
                asin = self.get_asin(data.get_attribute('href'))
                asin_code.add(asin)
                text = f'{asin}\n'
                f.write(text)
            start += 1

            print('Total unique asin', len(asin_code))
        f.close()
        driver.quit()
if __name__ == '__main__': #give your url to scrap
    scrap = Scrapper()
    scrap.scrap(1, 400)
