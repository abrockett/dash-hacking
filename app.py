# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import psycopg2
import os

connection_string = os.getenv("CONNECTION_STRING")
try:
    connection = psycopg2.connect(connection_string)
except:
    print("Can't connect to the database")

cursor = connection.cursor()

cursor.execute("""select * from subscription_dimension where created_at > '2017-12-06' LIMIT 10""")

rows = cursor.fetchall()
for row in rows:
    print ("   ", row[5], "   ", row[6])

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)