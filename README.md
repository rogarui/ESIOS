# ESIOS

Guía para aprender a utilizar la API de ESIOS de Red Eléctrica con Python.  
Nos vamos a centrar en cómo conseguir información de los distintos indicadores de la API y graficar los datos de una forma sencilla, así como descargar archivos.  

_Es cierto que para usar esta guía no se necesita un gran conocimiento de Python pero sí una mínima base para poder tocar y trastear con comodidad._

## 📔 Documentación oficial
Esta es la documentación oficial proporcionada por REE para el uso de su API.  
https://api.esios.ree.es/

## 🔑 Obtener un token

Para poder utilizar esta API se deberá solicitar un token personal enviando un correo a consultasios@ree.es.  
Suelen ser rápidos en contestar 🤞

## 🧾 Listado de indicadores y archivos 
En el archivo [lista_indicadores_archivos.py](examples/lista_indicadores_archivos.py) encontraréis el código para obtener la lista de indicadores y de archivos junto con su _id_.  
Los archivos varían dependiendo del día que busquemos, por eso en el código se ha implementado una búsqueda por fecha.  

Este _id_ es muy importante ya que el es que luego usaremos en las llamadas para rescatar la información de la API.  

Obtendremos algo así:  

 nombre | id | tipo_archivo | fecha_publicacion | url_descarga |
| :----: | :----: | :----: |  :----: | :----: |
| C2_PrecioFinal | 187 | zip | [2023-10-10] | /archives/187/download?date=2023-09-16T23%3A59... |
| REE_BalancingEnerBids | 181 | csv | [2023-09-16, 2023-09-17] | /archives/181/download?date=2023-09-16T23%3A59... |
| ... | ... | ... | ... | ... |


 nombre | id |
| :----: | :----: |
| Generación programada PBF Hidráulica UGH | 1 |
| Generación programada PBF Hidráulica no UGH | 2 |
| ... | ... |

_Se han añadido unas líneas para poder descargarlos en Excel (este ejemplo era un Excel, tocará poner el formato que corresponda), descomentar para que se ejecuten correctamente._

## ⬇️ Descarga de un archivo 

Para poder descargar un archivo de la API previamente debemos conocer su _id_.  
Como en el paso anterior lo hemos aprendido a obtener, simplemente usaremos este _id_ en el fichero [descarga_archivos.py](examples/descarga_archivos.py).  

También podemos usar la url obtenida de la lista de archivos para ver como hacer la llamada a la API.  

Si necesitamos descargar archivos de varios días, podemos usar el código [descarga_archivos_extra.py](examples/descarga_archivos_extra.py).

## 🔎 Búsqueda por indicador 

Para poder obtener información de un indicador de la API, previamente debemos conocer su _id_.  
La url para llamar a la API siempre tiene la misma estructura inicial, lo único que deberemos variar serán los parámetros con el fin de obtener la información de una forma o de otra.  

Lista de posibles parámetros:  

Name | Description |
| :----: | :----: |
| locale | Obtener traducciones para idiomas (es, en). Idioma por defecto: es |
| datetime | Una fecha determinada por la que filtrar los valores (formato iso8601) |
| start_date | Comienzo del intervalo de fechas para filtrar los valores de los indicadores (formato iso8601) |
| end_date | Fin del intervalo de fechas para filtrar los valores de los indicadores (formato iso8601) |
| time_agg | Cómo agregar valores de indicadores al agruparlos por tiempo. Valores aceptados: `sum`, `average`. Valor por defecto: `sum`. |
| time_trunc | Indica a la API cómo truncar las series temporales de datos. Valores aceptados: `five_minutes`, `ten_minutes`, `fifteen_minutes`, `hour`, `day`, `month`, `year`. |
| geo_agg | Cómo agregar valores de indicadores al agruparlos por geo_id. Valores aceptados: `sum`, `average`. Valor por defecto: `sum`. |
| geo_ids | Indica a la API los geoidentificadores por los que filtrar los datos. |
| geo_trunc | Indica a la API cómo agrupar los datos a nivel de geolocalización cuando se informa al geo_agg. Valores aceptados: `country`, `electric_system`, `autonomous_community`, `province`, `electric_subsystem`, `town` and `drainage_basin`. |

Para los siguientes ejemplos se van a usar el indicador `600` correspondiente al precio Spot y el indicador `602` corespondiente a energía asignada en mercado Spot diario en España.

### Búsqueda por rango de fecha  

Una vez obtenido el indicador deseado (`600`), simplemente usaremos el fichero [descarga_datos_por_fecha.py](examples/descarga_datos_por_fecha.py) para obtener los datos usando el filtro de fechas deseado.  

<img src="https://github.com/rogarui/ESIOS/blob/main/images/plot_spot_fecha.png" width=100% height=100%>


### Búsqueda por rango de fecha y agrupación/agregación temporal 

Adicionalmente al rango de fechas podemos incorporar un parámetro (`time_trunc`) para obtener los datos agrupados por días, meses, años...y esta agregación puede ser usando una media o la suma de los datos (`time_agg`).  

En este caso usaremos [descarga_datos_agregados.py](examples/descarga_datos_agregados.py) para obtener la energía negociada en el mercado diario por día, usando la media y la suma.  

Usando la suma  

<img src="https://github.com/rogarui/ESIOS/blob/main/images/plot_energia_suma.png" width=100% height=100%>  

Usando la media  

<img src="https://github.com/rogarui/ESIOS/blob/main/images/plot_energia_media.png" width=100% height=100%>  

### Búsqueda por país 

También podemos descargar los datos de un país en concreto directamente.  
La clave aquí es añadir el parámetro `geo_ids[]=X` donde _X_ será el _id_ del país en cuestión, dejo una lista:  

id | País |
| :----: | :----: |
| 1 | Portugal |
| 2 | Francia |
| 3 | España |
| 8824 | Reino Unido |
| 8825 | Italia |
| 8826 | Alemania |
| 8827 | Bélgica |
| 8828 | Países Bajos |


En este caso usaremos [descarga_datos_por_pais.py](examples/descarga_datos_por_pais.py)  

<img src="https://github.com/rogarui/ESIOS/blob/main/images/plot_spot_pais.png" width=100% height=100%>  

Como habeis podido ver, se trata de construir la url para hacer la llamada que mejor se adapte a lo que necesitamos. Lo podemos complicar todo lo que queramos, añadir varios países, indicadores, rangos temporales, eso dependerá de nuestra habilidad a la hora de saber tratar los datos después.

## 🖌️ Visualización con Plotly

Con los datos de la API y [Plotly](https://plotly.com/python/) podemos hacer gráficos mucho más avanzados como las siguientes:  


[generacion_PV_provincias.py](examples/generacion_PV_provincias.py)  

<img src="https://github.com/rogarui/ESIOS/blob/main/images/plot_pv.png" width=50% height=50%>  

Precio spot en España (proximamente)

<img src="https://media.licdn.com/dms/image/D4E22AQHGugcl5Btimg/feedshare-shrink_1280/0/1684750873475?e=1707350400&v=beta&t=S2D0OoL-WYJfR0_TYPfN4WBa-lPMk0Pewe4Kv7elT7s" width=50% height=50%>





