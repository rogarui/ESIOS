# ESIOS

Guiá para poder entender y aprender a utilizar la API de ESIOS de Red Eléctrica con Python.  
Nos vamos a centrar en como conseguir información de los distintos indicadores de la API y como descargarnos archivos.

## Documentación oficial
https://api.esios.ree.es/

## Obtener un token

Para poder utilizar esta API se deberá solicitar un token personal enviando un correo a consultasios@ree.es.  
Suelen ser rápidos en contestar 🤞

## Listado de indicadores y archivos
En el archivo [lista_indicadores_archivos.py](examples/lista_indicadores_archivos.py) encontrareis el código para obtener la lista de indicadores y de archivos junto con su _id_.  
Los archivos varían dependiendo del día que busquemos, por eso en el código se ha implementado una busqueda por fecha.  

Este _id_ es muy importante ya que es que luego usaremos en las llamadas para rescatar la información de la API.

PD: Se han añadido unas lineas para poder descargarlos en excel (descomentar para que se ejecuten correctamente).

## Descarga de un archivo

## Busqueda por indicador



