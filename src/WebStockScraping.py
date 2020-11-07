#!/usr/bin/env python

import urllib
import utils
import whois
import re
import csv
import os
import builtwith
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class WebStockScraping:

    def __init__(self, robots=True, delay=True):
        self.url_page = "http://www.bolsa.es/"
        self.robots = robots
        self.delay = delay
        self.links = []
        self.ultima_transaccion = []
        self.volumen = []
        self.max_diario = []
        self.min_diario = []
        self.currentDir = os.path.dirname(__file__)
        self.filename = "bolsa_ibex_35.csv"
        self.filePath = os.path.join(self.currentDir, self.filename)
        self.ticker = []
        self.nombre = []
        self.img_count = 0

        """ Previous phase to evaluate the following aspects:"""

        # 1) file robots.txt
        # 2) sitemap,
        # 3) size,
        # 4) technology used
        
        #print("\n Technology Used: ", builtwith.parse('http://www.bolsa.es/'), "\n")

        # 5) owner
        print(whois.whois(self.url_page))

        self.soup = utils.parse_html_soup(self.url_page, self.robots, self.delay)

    def show_html(self):
        print(self.soup.prettify())

    def show_tickers(self):
        """ Print Ticker and href for Ibex 35 Companies"""

        l_span = self.soup.find_all('span', {'style': re.compile(r"position:absolute;left:0px")})
        s_span = self.soup.find_all('span', {'style': re.compile(r"position:absolute;left:90px")})
        for span, span_aux in zip(l_span, s_span):
            #print(span.a.text, span.a['href'], span_aux.a.text)
            self.ticker.append(span.a.text)
            self.nombre.append(span_aux.a.text)
            self.get_span_values(span.a['href'])
            self.generate_historical_histogram(span.a['href'])
            #self.links.append(span.a['href'])
            #print(self.links)
        self.write_csv()
        self.generate_histogram()
        """print(self.ultima_transaccion)
        print(self.volumen)
        print(self.max_diario)
        print(self.min_diario)"""

    def get_span_values(self, url):
        soup_links = utils.parse_html_soup(self.url_page+url, False, self.delay)
        l_span = soup_links.find_all('span', {'style': re.compile(r"position:absolute;left:23px")})
        for span in l_span:
            if "Última transacción" in span.text:
                self.ultima_transaccion.append(float(re.findall("\d+(?:\.\d+)?", span.text)[0]))
            elif "Volumen" in span.text:
                self.volumen.append(float(re.findall("\d+(?:\.\d+)?", span.text)[0]))
            elif "Máximo diario" in span.text:
                self.max_diario.append(float(re.findall("\d+(?:\.\d+)?", span.text)[0]))
            elif "Mínimo diario" in span.text:
                self.min_diario.append(float(re.findall("\d+(?:\.\d+)?", span.text)[0]))
            else:
                pass
            
    def write_csv(self):
        with open(self.filePath, 'w', newline='') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=["Ticker", "Nombre", "Última transaccion", "Volumen", "Máximo diario", "Mínimo diario"])
            writer.writeheader()
            writer = csv.writer(csvFile)
            for i in range(len(self.ultima_transaccion)):
                writer.writerow([self.ticker[i], self.nombre[i], self.ultima_transaccion[i], self.volumen[i], self.max_diario[i], self.min_diario[i]])
    
    def write_csv_hist(self, filePath, dia, cierre, cambio, cambio_porc, maximo, minimo, volumen):
        with open(filePath, 'w', newline='') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=["DÍA", "CIERRE", "CAMBIO", "CAMBIO%", "MÁXIMO", "MÍNIMO", "VOLUMEN"])
            writer.writeheader()
            writer = csv.writer(csvFile)
            for col1, col2, col3, col4, col5, col6, col7 in zip(dia, cierre, cambio, cambio_porc, maximo, minimo, volumen) :
                writer.writerow([col1.text, col2.text, col3.text, col4.text, col5.text, col6.text, col7.text])
                #print(col1.text)
            #for i in range(len(self.ultima_transaccion)):
                #writer.writerow([self.ticker[i], self.nombre[i], self.ultima_transaccion[i], self.volumen[i], self.max_diario[i], self.min_diario[i]])


    def generate_historical_histogram(self, url):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get(self.url_page+url)
        select = Select(driver.find_element_by_id('IdMesI'))
        #select by visible text
        #select.select_by_visible_text('ENE')
        #select by value 
        select.select_by_value('1')
        #select = Select(driver.find_element_by_id('IdMesF'))
        #select.select_by_value('1')
        drp = driver.find_element_by_id('Enviar')
        drp.click();
        
        dia = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:2px')]")
        cierre = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:110px')]")
        cambio = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:210px')]")
        cambio_porc = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:310px')]")
        maximo = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:410px')]")
        minimo = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:510px')]")
        volumen = driver.find_elements_by_xpath("//span[contains(@style, 'position:absolute;left:610px')]")
        
        filePath = os.path.join(self.currentDir, self.nombre[self.img_count]+".csv")
        self.write_csv_hist(filePath, dia, cierre, cambio, cambio_porc, maximo, minimo, volumen)
           
        img_capture = driver.find_element_by_id('IdObjetoGrafica').get_attribute("src")
        urllib.request.urlretrieve(img_capture, self.nombre[self.img_count]+".png")
        self.img_count = self.img_count + 1;
        
        driver.close()