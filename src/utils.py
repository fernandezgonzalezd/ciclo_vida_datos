#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import urllib.robotparser as robot_parser
import time
import random

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
]


def parse_html_soup(url, robots=True, delay=True):
    """Download the web page and parse it using BeautifulSoup.

    Keyword arguments:
        url -- url web page
        robots -- disallowed by robots.txt?
        delay --  delay for retry
    """
    soup = None

    if robots:
        allowed = check_robots_txt(url, delay)
        if not allowed:
            print(url, "\nAccess DENIED by robots.txt")
            return

    if delay:
        delay_random(url=url)

    web_page = download_page(url)
    if web_page is not None:
        # Pulling data out of HTML
        soup = BeautifulSoup(web_page.content, 'html.parser')
    return soup


def hlcheck_robots_txt(url, delay=True):
    if delay:
        delay_random(url=url)
    rp = robot_parser.RobotFileParser()
    rp.set_url(url + "robots.txt")
    rp.read()
    if rp.can_fetch("*", url):
        return True
    else:
        return False


def download_page(url):
    user_agent = random.choice(USER_AGENT_LIST)

    return requests.get(url, headers={'User-Agent': user_agent})


def delay_random(min=1.1, max=3.0, url=""):
    """
     delay the execution of function using sleep()
    """
    seconds = random.uniform(min, max)
    print("delay_random (" + url + ")", seconds)
    time.sleep(seconds)
