from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv



PATH="C:\Program Files (x86)\chromedriver.exe"

driver= webdriver.Chrome(PATH)
url="https://www.jumia.com.ng/flash-sales/"
driver.get(url)

def main():
    # URL = 'https://www.jumia.com.ng/flash-sales/'
    categories=[
    'Computing',
    'Electronics',
    'Sporting Goods',
    'Phones & Tablets',
    'Fashion',
    'Home & Office',
    'Grocery',
    'Health & Beauty']

    # oldCsv = []
    # with open('headers.csv', 'r', encoding="utf-8") as csvfile:
    #     csvReader = csv.reader(csvfile, delimiter=',')
    #     for row in csvReader:
    #         oldCsv.append(row)
  

#   generates page source for different category

    for category in categories:
        search= driver.find_element(By.ID,'fi-q')

        search.send_keys(category)
        search.clear()
        search.send_keys(Keys.RETURN)
        scrape=driver.page_source
        soup1=BeautifulSoup(scrape, "html.parser") 
        soup2= BeautifulSoup(soup1.prettify(), "html.parser")

        oldCsv = []
        with open('dataset3.csv', 'r', encoding="utf-8") as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',')
            for row in csvReader:
                    oldCsv.append(row)

        for entry in soup2.find_all('div', {'class': 'info'}):
            title = entry.find('h3', {'class': 'name'}).text.strip()
            discount_price= entry.find('div', {'class': 'prc'}).text.strip()
            original_price= getattr(entry.find('div', {'class': 's-prc-w'}),'text','None')
            percentage_dsc= getattr(entry.find('div', {'class': 'bdg _dsct _sm'}),'text','None')
            rating=getattr(entry.find('div', {'class': 'stars _s'}),'text','None')
            raters=getattr(entry.find('div', {'#text'}),'text','None')

            data= [title,discount_price,original_price,percentage_dsc,rating,raters]

            # appending file
            addData = True

            for _ in oldCsv:
                if _[0] == title:
                    addData = False

            if addData:
                with open('dataset3','a+', newline='', encoding='UTF8') as f:
                    writer=csv.writer(f)
                    writer.writerow(data)
                          
            # with open('dataset1.csv','a+', newline='', encoding='UTF8') as f:
            #     writer=csv.writer(f)
            #     writer.writerow(data)


    time.sleep(2)
    driver.quit()


def scrape_pages(url) -> None:
    max_pages = 3
    current_page = 1

    # Loop through all pages dynamically and build the url using the page number suffix the website uses
    while current_page <= max_pages:
        current_page += 1
        print(f'{url}?page={current_page}')

  
#         # Get each page's html
        raw_html = f'{url}?page={current_page}'
        f"https://www.jumia.com.ng/{category}/?page={current_page}#catalog-listing
        soup = BeautifulSoup(raw_html.text, 'html.parser')

# #         # Find all table rows and from each table row get the needed data 
        for entry in soup.find_all('div', {'class': 'info'}):
            title = entry.find('h3', {'class': 'name'}).text.strip()
            discount_price= entry.find('div', {'class': 'prc'}).text.strip('â‚¦ ')
            original_price= getattr(entry.find('div', {'class': 's-prc-w'}),'text','None')
            original_price= original_price.strip('â‚¦ %')
            percentage_dsc= getattr(entry.find('div', {'class': 'bdg _dsct _sm'}),'text','None')
            rating=(entry.find('div', {'class': 'rev'}),'text','None')
            data= [title,discount_price,original_price,percentage_dsc]
            
            with open('dataset1.csv','a+', newline='', encoding='UTF8') as f:
                writer=csv.writer(f)
                writer.writerow(data)
            

        # time.sleep(10) # sleep before scraping next page to not send too many requests at once 
        # # current_page += 1
        print('\n\n') # Clearing console up 




if __name__ == '__main__':
    while True:
        main()
        time_wait=60
        print(f'Waiting {time_wait} seconds. . .')
        time.sleep(time_wait)
