# Práctica Tipología y Ciclo de vida de datos 1

# WebStockScrapingMultiThread

Práctica 1: Práctica Tipología y Ciclo de vida de datos 1
Práctica de generación de dataset mediante web scraping

El DOI de publicación en Zenodo es:

# Alumnos

* Waziri Ajibola Lawal
* David Fernández González

## Ejecución
Para ejecutar mainSCript.py hay que tener instalados los siguientes componentes:
- **BeautifulSoup**             
- **threading**           
- **selenium**      

El webdriver usado para selenium es **chromedriver**. Es necesario cambiar el *executable_path* en el archivo 
WebStockScrapingMultiThread.py, línea 115

En el proceso de llamadas se usa:   

- Check Robots.txt file
- Random User Agents
- Delay Random entre llamadas
- Threads: para hacer más rápdia la ejecución recoger la información con selenium
## Ficheros del código fuente

   * **src/utils.py**: funciones para comprobar el robots.txt, parsear la página web, random delays, etc
   * **src/WebStockScrapingMultiThread.py**: contiene la clase que  recoge la información de bolsa.es, y de cada compañía
   * **src/WebStockScraping.py** mismo código que WebStockScrapingMultiThread, pero sin ejecución en paralelo, más lento 


## Objetivos

  Los objetivos concretos de esta práctica son:
- Aprender a aplicar los conocimientos adquiridos y su capacidad de resolución de
problemas en entornos nuevos o poco conocidos dentro de contextos más
amplios o multidisciplinarios.
- Saber identificar los datos relevantes que su tratamiento aporta valor a una
empresa y la identificación de nuevos proyectos analíticos.
- Saber identificar los datos relevantes para llevar a cabo un proyecto analítico.
- Capturar datos de diferentes fuentes de datos (tales como redes sociales, web
de datos o repositorios) y mediante diferentes mecanismos (tales como queries,
API y scraping).
- Actuar con los principios éticos y legales relacionados con la manipulación de
datos en función del ámbito de aplicación.
- Desarrollar la capacidad de búsqueda, gestión y uso de información y recursos
en el ámbito de la ciencia de datos.

## Descripción de la Práctica a realizar
  El objetivo de esta actividad será la creación de un dataset a partir de los datos
contenidos en una web. Para su realización, se deben cumplir los siguientes puntos:
1. Contexto. Explicar en qué contexto se ha recolectado la información. Explique
por qué el sitio web elegido proporciona dicha información.
2. Definir un título para el dataset. Elegir un título que sea descriptivo.
3. Descripción del dataset. Desarrollar una descripción breve del conjunto de datos
que se ha extraído (es necesario que esta descripción tenga sentido con el título
elegido).
4. Representación gráfica. Presentar una imagen o esquema que identifique el
dataset visualmente
5. Contenido. Explicar los campos que incluye el dataset, el periodo de tiempo de
los datos y cómo se ha recogido.
6. Agradecimientos. Presentar al propietario del conjunto de datos. Es necesario
incluir citas de investigación o análisis anteriores (si los hay).
7. Inspiración. Explique por qué es interesante este conjunto de datos y qué
preguntas se pretenden responder.
8. Licencia. Seleccione una de estas licencias para su dataset y explique el motivo
de su selección:
○ Released Under CC0: Public Domain License
○ Released Under CC BY-NC-SA 4.0 License
○ Released Under CC BY-SA 4.0 License
○ Database released under Open Database License, individual contents
under Database Contents License
○ Other (specified above)
○ Unknown License
9. Código. Adjuntar el código con el que se ha generado el dataset, preferiblemente
en Python o, alternativamente, en R.
10. Dataset. Publicación del dataset en formato CSV en Zenodo (obtención del DOI)
con una breve descripción
