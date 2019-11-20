from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.melon.com/chart/month/index.htm#params%5Bidx%5D=1&params%5BrankMonth%5D=201910&params%5BisFirstDate%5D=false&params%5BisLastDate%5D=true")

page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
table = soup.find('tbody')

songlist = table.find_all('tr')
songID = []
for song in songlist:
    songID.append(song.get('data-song-no'))
del songID[0]