from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import time
import urllib.request

browser = webdriver.Chrome('.\chrome crowling test\chromedriver.exe')

delay=2
browser.implicitly_wait(delay)

start_url  = 'https://music.youtube.com'
browser.get(start_url)  
browser.maximize_window()


browser.find_elements_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]')[0].click()
browser.find_elements_by_id('input')[1].send_keys('Eminem Rap god') #검색창 영역에 원하는 youtuber입력
browser.find_elements_by_id('input')[1].send_keys(Keys.RETURN)#엔터



 
# url = "https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS"
# req = urllib.request.Request(url)
# sourcecode = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(sourcecode, "html.parser")
  
# for href in soup.find("div", class_="w_news_list").find_all("li"):
#     print(href.find("a")["href"])
