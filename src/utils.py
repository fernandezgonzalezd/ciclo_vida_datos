#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


def parse_html_soup(url, robots=True, delay=True):
    """Download the web page and parse it using BeautifulSoup.

    Keyword arguments:
        url -- url web page
        robots --
        delay --  delay for retry
    """
    soup = None
    web_page = download_page(url)
    if web_page is not None:
        # Pulling data out of HTML
        soup = BeautifulSoup(web_page.content, 'html.parser')

    return soup


def download_page(url):
    return requests.get(url)
