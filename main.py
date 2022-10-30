from bs4 import BeautifulSoup
from pip import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


PATH="C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(PATH)

url="https://www.jumia.com.ng/flash-sales/"
driver.get(url)
print(driver.title)
search= driver.find_element(By.ID,'fi-q')

search.send_keys("Nike")
search.send_keys(Keys.RETURN)


# print(driver.page_source)

time.sleep(5)

driver.quit()