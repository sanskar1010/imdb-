import pandas as pd
from bs4 import BeautifulSoup
import requests
url='https://weather.com/en-IN/weather/weekend/l/67389df55ad6875ef4646dbaf9f944e34435e8401fccfce6d7b4698e39b4401b'
html_text=requests.get(url).content
soup=BeautifulSoup(html_text,'lxml')
details=soup.find_all('div','DailyContent--DailyContent--1yRkH')
for detail in details:
    d={}
    temperature=detail.find('span','DailyContent--temp--1s3a7').get_text()
    time=detail.find('h3','DailyContent--daypartName--3emSU').get_text()
    rain_percentage=detail.find('span','DailyContent--value--1Jers').get_text()
    winds=detail.find('span','Wind--windWrapper--3Ly7c DailyContent--value--1Jers DailyContent--windValue--JPpmk')
    wind_details=winds.find_all('span')
    direction=wind_details[0].get_text()
    speed=wind_details[1].get_text()
    measure=wind_details[2].get_text()
    d['wind speed'] = direction + speed + measure
    d['time'] = time.split('|')[1].strip()
    d['date'] = time.split('|')[0].strip()
    d['rain percentage'] = rain_percentage
    d['temperature'] = temperature
    print(d)

  
