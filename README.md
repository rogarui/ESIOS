# ESIOS

Guía para aprender a utilizar la API de ESIOS de Red Eléctrica con Python.  
Nos vamos a centrar en como conseguir información de los distintos indicadores de la API y como descargar archivos.

## Documentación oficial
https://api.esios.ree.es/

## Obtener un token

Para poder utilizar esta API se deberá solicitar un token personal enviando un correo a consultasios@ree.es.  
Suelen ser rápidos en contestar 🤞

## Listado de indicadores y archivos 🧾🧾
En el archivo [lista_indicadores_archivos.py](examples/lista_indicadores_archivos.py) encontrareis el código para obtener la lista de indicadores y de archivos junto con su _id_.  
Los archivos varían dependiendo del día que busquemos, por eso en el código se ha implementado una busqueda por fecha.  

Este _id_ es muy importante ya que es que luego usaremos en las llamadas para rescatar la información de la API.  

Obtendremos algo así:  

 nombre | id | tipo_archivo | fecha_publicacion | url_descarga |
| :----: | :----: | :----: |  :----: | :----: |
| C2_PrecioFinal | 187 | zip | [2023-10-10] | /archives/187/download?date=2023-09-16T23%3A59... |
| REE_BalancingEnerBids | 181 | csv | [2023-09-16, 2023-09-17] | /archives/181/download?date=2023-09-16T23%3A59... |


 nombre | id |
| :----: | :----: |
| Generación programada PBF Hidráulica UGH | 1 |
| Generación programada PBF Hidráulica no UGH | 2 |

PD: Se han añadido unas lineas para poder descargarlos en excel (descomentar para que se ejecuten correctamente).

## Descarga de un archivo ⬇️⬇️

Para poder descargar un archivo de la API previamente debemos conocer su _id_.  
Como en el paso anterior lo hemos aprendido a obtener, simplemente usaremos este _id_ en el fichero [descarga_archivos.py](examples/descarga_archivos.py).  

También podemos usar la url obtenida de la lista de archivos para ver como hacer la llamada a la API.  

Si necesitamos descargar archivos de varios días, podemos usar el código [descarga_archivos_extra.py](examples/descarga_archivos_extra.py).

## Busqueda por indicador 🔎🔎



