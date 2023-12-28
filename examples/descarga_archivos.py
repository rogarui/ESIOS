import requests

#Token ESIOS
esios_token = ''

#Este ejmplo es para descargar el i90
address = "https://api.esios.ree.es/archives/34/download?date_type\u003ddatos\u0026end_date\u003d2023-09-16T23%3A59%3A59%2B00%3A00\u0026locale\u003des\u0026start_date\u003d2023-09-16T00%3A00%3A00%2B00%3A00"

resp = requests.get(address, headers={'x-api-key' : '%s' %(esios_token),
                                             'Authorization' : 'Token token=%s' %(esios_token)})

with open("fichero.zip", "wb") as fd:
    fd.write(resp.content)
