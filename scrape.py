#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4 as bs
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


# In[2]:


data = {
    'name' : [],
    'meaning' : [],
    'gender' : []
}


# In[9]:


for page in range(1, 214):  # English names has 213 pages 
    sauce = urllib.request.urlopen('https://www.momjunction.com/baby-names/english/page/' + str(page)).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    table = soup.find('table')
    table_rows = table.find_all('tr')[1:-1]
    for tr in table_rows:
        td = tr.find_all('td')[0:3]
        row = [i.text for i in td]
        if len(row) > 1:
            data['name'].append(row[0])
            data['meaning'].append(row[1])
            data['gender'].append(row[2])


# In[3]:


file = pd.DataFrame(data)
file.to_csv("english_name.csv")


# In[11]:


data2 = {
    'name' : [],
    'meaning' : [],
    'gender' : []
}
for page in range(1, 19):  # African names has 18 pages 
    sauce = urllib.request.urlopen('https://www.momjunction.com/baby-names/african/page/' + str(page)).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    table = soup.find('table')
    table_rows = table.find_all('tr')[1:-1]
    for tr in table_rows:
        td = tr.find_all('td')[0:3]
        row = [i.text for i in td]
        if len(row) > 1:
            data2['name'].append(row[0])
            data2['meaning'].append(row[1])
            data2['gender'].append(row[2])


# In[12]:


file2 = pd.DataFrame(data2)
file2.to_csv("african_name.csv")


# In[14]:


data3 = {
    'name' : [],
    'meaning' : [],
    'gender' : []
}
for page in range(1, 65):  # Hebrew names has 64 pages 
    sauce = urllib.request.urlopen('https://www.momjunction.com/baby-names/hebrew/page/' + str(page)).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    table = soup.find('table')
    table_rows = table.find_all('tr')[1:-1]
    for tr in table_rows:
        td = tr.find_all('td')[0:3]
        row = [i.text for i in td]
        if len(row) > 1:
            data3['name'].append(row[0])
            data3['meaning'].append(row[1])
            data3['gender'].append(row[2])
            
file3 = pd.DataFrame(data3)
file3.to_csv("hebrew_name.csv")

