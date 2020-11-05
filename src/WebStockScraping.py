#!/usr/bin/env python

import utils
import whois


class WebStockScraping:

    def __init__(self, robots=False, delay=False):
        self.url_page = "http://www.bolsa.es/"
        self.robots = robots
        self.delay = delay

        """ Previous phase to evaluate the following aspects:"""

        # 1) file robots.txt
        # 2) sitemap,
        # 3) size,
        # 4) technology used
        # 5) owner
        print(whois.whois(self.url_page))

        self.headers = {"User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
        # We will need robots and delay later
        self.soup = utils.parse_html_soup(self.url_page, self.robots, self.delay)

    def show_html(self):
        print(self.soup.prettify())
