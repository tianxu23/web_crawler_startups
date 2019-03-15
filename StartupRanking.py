# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:47:42 2018

@author: Vincent Xu
"""

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

print('hello world')
name = []
sr_score = []
description = []
rank = []
country = []
cookies="__cfduid=dec88b28e8e961165997ef60680fe403b1534861991; _ga=GA1.2.1626646993.1534861991; __zlcmid=o0haD3bcFUuqHC; _gid=GA1.2.422863630.1536078869; extensionClosed=true; PHPSESSID=e9u5uahsfqgo95gmrlrqn0a456; _hjIncludedInSample=1; cf_clearance=4708dc1b3f0f1d43b1bc6315d312daba539a4408-1536243521-3600-150"
i = 0
print(i)

while True:
    try:
        if i == 0:
            source = requests.get('https://www.startupranking.com/top').text
			print(i)
        else:
			i=i+1
			print(i)
            headers = {
            'Accept':'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
            'Cache-Control':'max-age=0',
            'Cookie': cookies,
            'Host':'www.startupranking.com',
            'Referer':'https://www.startupranking.com/top/0/'+str(i),
            'Upgrade-Insecure-Requests':'1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'      
                   }
            source = requests.get('https://www.startupranking.com/top/0/'+str(i+1),headers=headers).text
            
        soup = BeautifulSoup(source, 'lxml')
        
        
        for n in soup.find('tbody',class_='ranks').find_all('div',class_='name'):
        
            name.append(n.text)
            
            
        
        for s in soup.find('tbody',class_="ranks").find_all('td',class_= 'tright sr-score'):
            sr_score.append(s.text.strip())
        
        
        
        for d in soup.find('tbody',class_="ranks").find_all('td',class_= 'tleft description'):
               description.append(d.text.strip())
               
        
        
        for r in soup.find('tbody',class_="ranks").find_all('div', class_= 'country-rank'):
               rank.append(r.text)
        
        
        
        for c in soup.find('tbody',class_="ranks").find_all('img'):
               country.append(c.get('title'))
               
        i=i+1
           
    except:
        break
           

a = np.array([name,sr_score,description,country[1::2],rank])


starts_ups = pd.DataFrame(a.T,columns = ['Name','SR_Score','Description','Country','Country_rank'])   

starts_ups



