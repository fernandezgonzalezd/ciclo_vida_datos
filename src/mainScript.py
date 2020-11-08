#!/usr/bin/env python

import sys
import time

from WebStockScraping import WebStockScraping

__author__ = "Waziri Ajibola Lawal, David Fernández González"
__email__ = "wlawal@uoc.edu, dfernandezgonz@uoc.edu"

sys.path.append(' M2.851 - Tipología y ciclo de vida de los datos  ')

# store starting time
begin = time.time()

webStockScraping = WebStockScraping(robots=True, delay=True)


webStockScraping.show_tickers()
#webStockScraping.show_html()

end = time.time()

print(f"Total runtime of the program is {end - begin}")
