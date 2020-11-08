#!/usr/bin/env python

import urllib

from selenium.common.exceptions import NoSuchElementException

import utils
import whois
import re
import csv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import shutil
import threading


class WebStockScrapingMultiThread:

    def __init__(self, robots=True, delay=True):
        self.urlPage = "http://www.bolsa.es/"
        self.robots = robots
        self.delay = delay
        self.links = []
        self.ultimaTransaccion = []
        self.volumen = []
        self.maxDiario = []
        self.minDiario = []
        self.currentDir = os.path.dirname(__file__)
        self.fileName = "Bolsa_ibex_35.csv"
        self.filePath = os.path.join(self.currentDir, self.fileName)
        self.ticker = []
        self.nombre = []

        """ Previous phase to evaluate the following aspects:"""

        # 1) file robots.txt
        # 2) sitemap,
        # 3) size,
        # 4) technology used

        # print("\n Technology Used: ", builtwith.parse('http://www.bolsa.es/'), "\n")

        # 5) owner
        print(whois.whois(self.urlPage))

        self.soup = utils.parse_html_soup(self.urlPage, self.robots, self.delay)

    def show_html(self):
        print(self.soup.prettify())

    def show_tickers(self):
        """ Print Ticker and href for Ibex 35 Companies"""

        l_span = self.soup.find_all('span', {'style': re.compile(r"position:absolute;left:0px")})
        s_span = self.soup.find_all('span', {'style': re.compile(r"position:absolute;left:90px")})
        my_threads = []

        for span, span_aux in zip(l_span, s_span):
            self.ticker.append(span.a.text)
            self.nombre.append(span_aux.a.text)
            self.get_span_values(span.a['href'])
            t = threading.Thread(target=self.generate_historical_histogram, args=(span.a['href'], span_aux.a.text, ))
            t.start()
            my_threads.append(t)

        for x in my_threads:
            x.join()

        self.write_csv()

    def get_span_values(self, url):
        soup_links = utils.parse_html_soup(self.urlPage + url, False, self.delay)
        l_span = soup_links.find_all('span', {'style': re.compile(r"position:absolute;left:23px")})
        for span in l_span:
            if "Última transacción" in span.text:
                self.ultimaTransaccion.append(float(re.findall("\d+(?:\.\d+)?", span.text)[0]))
            elif "Volumen" in span.text:
                self.volumen.append(float(re.findall("\d+(?:\.\d+)?", span.text)[0]))
            elif "Máximo diario" in span.text:
                self.maxDiario.append(float(re.findall("\d+(?:\.\d+)?", span.text)[0]))
            elif "Mínimo diario" in span.text:
                self.minDiario.append(float(re.findall("\d+(?:\.\d+)?", span.text)[0]))
            else:
                pass

    def write_csv(self):
        with open(self.filePath, 'w', newline='') as csvFile:
            writer = csv.DictWriter(csvFile,
                                    fieldnames=["Ticker", "Nombre", "Última transaccion", "Volumen", "Máximo diario",
                                                "Mínimo diario"])
            writer.writeheader()
            writer = csv.writer(csvFile)
            for i in range(len(self.ultimaTransaccion)):
                writer.writerow(
                    [self.ticker[i], self.nombre[i], self.ultimaTransaccion[i], self.volumen[i], self.maxDiario[i],
                     self.minDiario[i]])

    def write_csv_hist(self, name, dia, cierre, cambio, cambio_porc, maximo, minimo, volumen):
        file_path = os.path.join(self.currentDir, "output/", name + ".csv")

        with open(file_path, 'w', newline='') as csvFile:
            writer = csv.DictWriter(csvFile,
                                    fieldnames=["DÍA", "CIERRE", "CAMBIO", "CAMBIO%", "MÁXIMO", "MÍNIMO", "VOLUMEN"])
            writer.writeheader()
            writer = csv.writer(csvFile)
            print("write_csv_hist csv " + file_path)
            for col1, col2, col3, col4, col5, col6, col7 in zip(dia, cierre, cambio, cambio_porc, maximo, minimo,
                                                                volumen):
                writer.writerow([col1.text, col2.text, col3.text, col4.text, col5.text, col6.text, col7.text])

    def generate_historical_histogram(self, url, name):
        # Windows
        # driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(executable_path="/home/david/Software/chromedriver_linux64/chromedriver")
        driver.get(self.urlPage + url)
        select = Select(driver.find_element_by_id('IdMesI'))
        select.select_by_value('1')
        drp = driver.find_element_by_id('Enviar')
        drp.click()

        dia = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:2px')]")
        cierre = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:110px')]")
        cambio = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:210px')]")
        cambio_porc = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:310px')]")
        maximo = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:410px')]")
        minimo = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:510px')]")
        volumen = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:610px')]")

        self.write_csv_hist(name, dia, cierre, cambio, cambio_porc, maximo, minimo, volumen)

        try:
            img_capture = driver.find_element_by_id('IdObjetoGrafica').get_attribute("src")
            file_name = os.path.join(self.currentDir, "images/", name + ".png")
            with urllib.request.urlopen(img_capture) as response, open(file_name, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)

            print("Saving image " + file_name)

        except NoSuchElementException:
            print("error downloading image for " + name)

        driver.close()
