#!/usr/bin/env python

import sys
from WebStockScraping import WebStockScraping

__author__ = "Waziri Ajibola Lawal, David Fernández González"
__email__ = "wlawal@uoc.edu, dfernandezgonz@uoc.edu"

sys.path.append(' M2.851 - Tipología y ciclo de vida de los datos  ')


webStockScraping = WebStockScraping(robots=False, delay=False)


webStockScraping.show_tickers()
#webStockScraping.show_html()

print("--- FIN ---")
