# Práctica Tipología y Ciclo de vida de datos 1

## Autores

* Waziri Ajibola Lawal
* David Fernández González

## Descripción

Práctica  para la extracción de datos de la web [Bolsa.es](hhttp://www.bolsa.es/), y generar un _dataset_. Se ha realizado aplicando técnicas de _web scraping_ mediante el lenguaje de programación Python.

El DOI de publicación en Zenodo es: 

    dataset: 10.5281/zenodo.4262200
    images: 10.5281/zenodo.4262291

## Ejecución

Para ejecutar mainSCript.py hay que tener instalados los siguientes bibliotecas:

    pip3 install python-whois
    pip3 install shutil
    pip3 install selenium
    pip3 install beautifulsoup4

Y se podrá ejecutar con el siguiente comando
    
    python3 src/cmainScript.py 


El webdriver usado para selenium es **chromedriver**. Es necesario cambiar el *executable_path* en el archivo  WebStockScrapingMultiThread.py, línea 115

Durante la ejecución se realizan diferentes tareas:

- Comprobar el archivo Robots.txt
- Cambiar aleatoriamente de  User-Agents
- Hay un retraso aleatorio entre cada llamada
- Se usan Threads: para hacer más rápida la ejecución de recoger la información con selenium

## Ficheros del código fuente

   * **src/utils.py**: contiene funciones para comprobar el robots.txt, parsear la página web, random delays, etc
   * **src/WebStockScrapingMultiThread.py**: contiene la implementación multithread, que  recoge la información de cada compañía del Ibex 35 de bolsa.es
   * **src/WebStockScraping.py** mismo código que WebStockScrapingMultiThread, pero sin ejecución en threads (más lento)


## Recursos

1. Subirats, L., Calvo, M. (2019). Web Scraping. Editorial UOC.
2. Masip, D. (2010). El lenguaje Python. Editorial UOC.
3. Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
