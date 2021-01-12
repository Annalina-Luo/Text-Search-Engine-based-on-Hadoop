import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import urllib
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

for j in range(1800, 3500):
    url = "http://www.gutenberg.org/ebooks/%s" % j
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/74.0.3729.157 Safari/537.36'}

    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.text, "lxml")

    medicine_table = soup.find_all('h1', itemprop="name")

    for i in medicine_table:
        name = i.text
        print(name)
    print('---------')

    url_doc = "http://www.gutenberg.org/cache/epub/%s/pg" % j + "%s.txt" % j


    req = requests.get(url_doc, headers=headers)
    # print(req)
    # soup = BeautifulSoup(req.text, "lxml")
    # # print(soup)
    # medicine_table = soup.find_all('a', title='Download')
    file = r'D:\ebook\%s.txt' % name
    print('读到文件啦！')
    if name.find("\"") == -1 & name.find(":") == -1 & name.find("*") == -1 & name.find("?") == -1\
            & name.find("<") == -1 & name.find(">") == -1 & name.find("|") & name.find("/")== -1:
        with open(file, "wb") as code:
            code.write(req.content)
