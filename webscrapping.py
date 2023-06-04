#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup as bs

URL = 'https://proxyway.com/reviews'

for page in range(1, 4):
    print("\n")
    print("Sub Titles Page:", page, "\n")

    req = requests.get(f'{URL}/page/{page}')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('h3', class_='archive-list__title')

    for i, title in enumerate(titles):
        print(f"{i+1} {title.text}")


# In[17]:


import csv
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://proxyway.com/reviews'

data = []

for page in range(1, 4):
    print("\n")
    print("Sub Titles Page:", page, "\n")

    req = requests.get(f'{URL}/page/{page}')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('h3', class_='archive-list__title')

    for i, title in enumerate(titles):
        print(f"{i+1} {title.text}")
        data.append({
            'Page Number': f'Page {page}',
            'Title Number': f'Title {i+1}',
            'Title Name': title.text
        })

# Menyimpan data ke dalam file CSV
filename = 'proxywaydata.csv'
fieldnames = ['Page Number', 'Title Number', 'Title Name']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Data telah disimpan ke dalam file", filename)
