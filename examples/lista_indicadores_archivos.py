import pandas as pd
import requests



#Token ESIOS (introducir tu propio token)
esios_token = ''

address = "https://api.esios.ree.es/archives?date=2023-09-15T23:59:59+00:00"

resp = requests.get(address, headers={'x-api-key' : '%s' %(esios_token),
                                             'Authorization' : 'Token token=%s' %(esios_token)}).json()

name = []
id = []
tipo = []
publication_date = []
url = []

for i in range(0, len(resp['archives'])):
    name.append(resp['archives'][i]['name'])
    id.append(resp['archives'][i]['id'])
    tipo.append(resp['archives'][i]['archive_type'])
    publication_date.append(resp['archives'][i]['publication_date'])
    url.append(resp['archives'][i]['download']['url'])

archivos = pd.DataFrame({'nombre': name, 'id': id, 'tipo_archivo': tipo, 'fecha_publicacion': publication_date, 'url_descarga': url})

print(archivos)

#archivos.to_excel("./lista_esios_archivos.xlsx")


address = "https://api.esios.ree.es/indicators"

resp = requests.get(address, headers={'x-api-key' : '%s' %(esios_token),
                                             'Authorization' : 'Token token=%s' %(esios_token)}).json()


name = []
id = []


for i in range(0, len(resp['indicators'])):
    name.append(resp['indicators'][i]['name'])
    id.append(resp['indicators'][i]['id'])

indicadores = pd.DataFrame({'nombre': name, 'id': id})

print(indicadores)

#indicadores.to_excel("./lista_esios_indicadores.xlsx")
