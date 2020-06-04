# -*- coding: utf-8 -*-
import requests

from bs4 import BeautifulSoup

def fronda_parse_page(n, f):
    n = str(n)
    print("parsing " + n +" page of Fronda")
    URL = "https://www.fronda.pl/c/wiadomosci,1.html?page="+n+"&#comments"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    titles = soup.find_all(class_='tile-info')

    for title in titles:
        f.write('fronda\t' + title.find('a').find(text=True) + '\n')

def tvn24_parse_page(n, f):
    n = str(n)
    print("parsing " + n +" page of TVN24")
    URL = "https://tvn24.pl/najnowsze/"+n+"/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    titles = soup.find(class_='wide-column').find_all(class_='article-title')

    for title in titles:
        f.write('tvn24\t' + title.find(text=True) + '\n')

with open('big-data-tvn.tsv', 'w', encoding='utf-8') as f:
    # for i in range(3000):
        # fronda_parse_page(i, f)
    for i in range(5400):
        tvn24_parse_page(i, f)