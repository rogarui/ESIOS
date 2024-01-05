import pandas as pd
import numpy as np
import datetime as dt
from datetime import datetime, date, timedelta
import requests
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


#Token ESIOS
esios_token = ''

#FUNCION CONECTAR ESIOS
def esios_api(id_code, fecha_inicial, fecha_final, esios_token):
    try:
        address = "http://api.esios.ree.es/indicators/%s?start_date=%sT21:00:00Z&end_date=%sT23:00:00Z" % (id_code, fecha_inicial, fecha_final)

        print(address)
        resp = requests.get(address, headers={'x-api-key' : '%s' %(esios_token),
                                             'Authorization' : 'Token token=%s' %(esios_token)}).json()
    
        print(resp)
    except Exception as e:
        
        print(e)
    
    date = []
    value = []
    geo = []
    
    for i in range(0, len(resp['indicator']['values'])):
        date.append(resp['indicator']['values'][i]['datetime'][:19])
        value.append(resp['indicator']['values'][i]['value'])
        geo.append(resp['indicator']['values'][i]['geo_name'])

    data = pd.DataFrame({'fecha': date, 'valor': value, 'pais': geo})
    
    data['fecha'] = data['fecha'].str.replace('T',' ')
    
    #print(data)
    
    data['fecha'] = pd.to_datetime(data['fecha'])

    #data = data[data['fecha'].dt.year == año]
    #data['dia'] = data['fecha'].dt.day
    data = data.reset_index(drop=True)
    return data

codigo = 600
data = esios_api(codigo, "2024-01-01", "2024-01-05", esios_token)

print(data)


fig = px.line(data, x="fecha", y="valor", color='pais')
fig.update_layout({
                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                        
                        })
fig.show()
