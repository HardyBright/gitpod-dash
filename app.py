import dash
from dash import dash_table
from dash import dcc # dash core components
from dash import html

import pandas as pd

df = pd.read_csv('https://bit.ly/elements-periodic-table')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id = 'table-values-dropdown',
        options=[

            
        ]



    ),

    html.Div(dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ))
])
@app.callback(
    Output,
    Input(component_id='OK!', component_property='n_clicks'),
    State(component_id='index', component_property='value'),
    State(component_id='column', component_property='value'),
    State(component_id='values', component_property='value'),
)

app.run_server(debug=True, host="0.0.0.0")
