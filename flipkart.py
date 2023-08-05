import pandas as pd
import requests
from bs4 import BeautifulSoup
pages=362
flipkart=[]
for i in range(1,pages+1):
    url=f'https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}'
    html_text=requests.get(url).content
    soup=BeautifulSoup(html_text,'lxml')
    phones=soup.find_all('div','_3pLy-c row')
    for phone in phones:
        d={}
        phone_name=phone.find('div','_4rR01T').get_text()
        rating=phone.find('div','_3LWZlK').get_text()
        price=phone.find('div','_30jeq3 _1_WHN1').get_text()
        d['phone']=phone
        d['rating']=rating
        d['price']=price
        tables=phone.find('ul','_1xgFaf')
        table_rows=tables.find_all('li')
        d['RAM']=table_rows[0].get_text().split('|')[0].strip()
        d['ROM']=table_rows[0].get_text().split('|')[1].strip()
        d['Size']=table_rows[1].get_text()
        d['Rear Camera']=table_rows[2].get_text().split('|')[0].strip()
        d['Front Camera']=table_rows[2].get_text().split('|')[1].strip()
        d['Battery']=table_rows[3].get_text()
        d['Processor']=table_rows[4].get_text().split(' ')[0].strip()
        flipkart.append(d)
    print(flipkart)
