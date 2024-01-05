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
        address = "http://api.esios.ree.es/indicators/%s?start_date=%sT21:00:00Z&end_date=%sT23:00:00Z&time_trunc=month&time_agg=sum" % (id_code, fecha_inicial, fecha_final)

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

    data = pd.DataFrame({'fecha': date, 'valor': value, 'provincia': geo})
    
    data['fecha'] = data['fecha'].str.replace('T',' ')
    
    #print(data)
    
    data['fecha'] = pd.to_datetime(data['fecha'])

    #data = data[data['fecha'].dt.year == año]
    #data['dia'] = data['fecha'].dt.day
    data = data.reset_index(drop=True)
    return data

codigo = 1161

data = esios_api(codigo, "2010-01-31", "2023-12-01", esios_token)

df = data.pivot(index='fecha', columns='provincia', values='valor')
provincias = df.columns

# plotly setup
plot_rows=10
plot_cols=5
fig = make_subplots(rows=plot_rows, cols=plot_cols, subplot_titles=provincias)

# add traces
x = 0
for i in range(1, plot_rows + 1):
    for j in range(1, plot_cols + 1):
        #print(str(i)+ ', ' + str(j))
        try :
            fig.add_trace(go.Scatter(x=df.index,
                                        y=df[df.columns[x]].values,    
                                        name = df.columns[x],
                                        fill='tozeroy'
                                ),
                        row=i,
                        col=j)
            fig.update_layout({
                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                        
                        })
            #fig.update_yaxes(tickfont_family="Arial Black")
            #fig.update_xaxes(tickfont_family="Arial Black")

            x=x+1
        except:
            fig.add_trace(go.Scatter(x=[], y = []))
            x=x+1


# Format and show fig
fig.update_layout(height=2000, width=1500)
fig.for_each_annotation(lambda a: a.update(text=f'<b>{a.text}</b>'))
fig.update_layout(showlegend=False)
fig.update_layout(
    title=dict(text="Generación medida PV por provincia (MWh)",
               font=dict(size=30))
)
fig.show()
