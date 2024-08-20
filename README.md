# Proyecto de Scraping de Pluto TV

Este proyecto incluye dos scripts de scraping desarrollados en Python utilizando Selenium para extraer datos de la plataforma Pluto TV. Los datos extraídos se organizan en dos archivos Excel: uno para la sección "On Demand" y otro para "Live TV". Ambos archivos están formateados para una lectura clara y ordenada.

## Requisitos Previos

* Python 3.x
* Selenium
* Pandas
* Google Chrome
* [ChromeDriver]() compatible con la versión de Chrome instalada

## Estructura del Proyecto

* `plutotv-scrap.ipynb`: Script en Jupyter Notebook dividido en dos partes, una para la sección "On Demand" y otra para "Live TV".
* `On-Demand-PlutoTV.xlsx`: Archivo Excel con los datos de la sección "On Demand".
* `Live-TV-PlutoTV.xlsx`: Archivo Excel con los datos de la sección "Live TV".

## Ejecución

### 1. Scraping de la Sección "On Demand"

#### Descripción del Script

Este script extrae datos de la sección "On Demand" de Pluto TV, recorriendo todas las categorías de películas y series. Para cada elemento (película o serie), se obtiene la siguiente información:

* Título
* Año
* Calificación
* Descripción
* Género

Los datos se guardan en el archivo Excel `On-Demand-PlutoTV.xlsx`.

#### Tiempo de Ejecución

El script de la sección "On Demand" tiene un tiempo de ejecución de **130** **minutos**.

### 2. Scraping de la Sección "Live TV"

#### Descripción del Script

Este script extrae datos de la sección "Live TV" de Pluto TV, recorriendo todas las categorías de canales en vivo. Para cada canal, se obtiene la información de los programas en emisión, incluyendo:

* Título del programa
* Calificación
* Temporada
* Episodio
* Nombre del episodio
* Descripción

Los datos se guardan en el archivo Excel `Live-TV-PlutoTV.xlsx`.

#### Tiempo de Ejecución

El script de la sección "Live TV" tiene un tiempo de ejecución de **45 minutos**.

## Organización y Formateo de Datos

### Archivos Excel

* **On-Demand-PlutoTV.xlsx**: Contiene datos organizados de la sección "On Demand". Las columnas están diseñadas para facilitar la comprensión de la información.
* **Live-TV-PlutoTV.xlsx**: Contiene datos detallados de la sección "Live TV". Las columnas están organizadas para ofrecer una visión clara de los programas en emisión.

### Formateo

Los archivos Excel han sido formateados para asegurar una presentación clara y ordenada. Se ajustaron los anchos de las columnas, se aplicaron estilos básicos para destacar los encabezados, y se garantizó que toda la información relevante esté visible sin necesidad de ajustes adicionales.

## Notas Adicionales

* El tiempo de ejecución es exacto y puede variar según la velocidad de conexión a internet y el rendimiento del equipo.
* En el Script se dejo una variable para estimar el tiempo realizado exacto con nombre ***execution_time_total***.

## Agradecimientos

Quiero expresar mi agradecimiento a BB Media, Julieta y Lucía por la oportunidad de realizar este test. Estaría encantado de sumarme al equipo de BB Media, contribuir y seguir aprendiendo conjuntamente con el equipo.
