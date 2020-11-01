# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:42:28 2020

@author: WAZ
"""
import urllib
import requests
from bs4 import BeautifulSoup
import builtwith
import whois
import re


urltocheck = 'https://www.nike.com/es/w/hombre-ofertas-3yaepznik1'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

print(whois.whois('nike.com'))

print("\n Technology Used: ", builtwith.parse('http://example.webscraping.com/'), "\n")

req = requests.get(urltocheck)
soup = BeautifulSoup(req.content)
productList = soup.find_all('div', class_='product-card css-1ikfoht css-z5nr6i css-11ziap1 css-zk7jxt css-dpr2cn product-grid__card')

productArray = []

for i in productList:
    for n in i.find_all('a', class_ = 'product-card__img-link-overlay'):
        productArray.append(n['aria-label'])

print(productArray)


def download(url, user_agent='wswp', num_retries=2):
    print('Downloading:', url)
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(url).read().decode('utf-8', 'ascii')
    except urllib.error.URLError as e:
            print('Download error:', e.reason)
            html = None
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    # recursively retry 5xx HTTP errors
                    return download(url, user_agent, num_retries-1)
    return html


def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...