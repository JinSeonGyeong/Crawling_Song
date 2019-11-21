from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.melon.com/chart/month/index.htm#params%5Bidx%5D=1&params%5BrankMonth%5D=201910&params%5BisFirstDate%5D=false&params%5BisLastDate%5D=true")

songTagList = driver.find_elements_by_id('lst50')
songID = []
for i in songTagList:
    songID.append(i.get_attribute('data-song-no'))

import time
from tqdm import tqdm_notebook

summ = []
for i in range(0, len(songID)):
    driver.get(f'https://www.melon.com/song/detail.htm?songId={songID[i]}')
    summary = driver.find_element_by_xpath("//div[@id='d_video_summary']")
    s1 = summary.text
    s1 = s1.replace("\n", "")
    summ.append(s1)
    
    time.sleep(1)

summ
