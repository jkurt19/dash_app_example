#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(_name_)   
server = app.server
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
        
app.layout = html.Div(children=[       #layout of the dashboard. One writes it with html. 
    html.H1(children='Hello Dash'),

    html.Div(children='''              
        Dash: A web application framework for Python.
    '''),
#.div, from trip advisor you know everything nowadays is a .div
#children: big heather...
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

# the graph that you can visualize in the dashboard. two important things: data (two elements that are the axis) 
#and layout of graph. 

if __name__ == '__main__':
    app.run_server(debug=False)

