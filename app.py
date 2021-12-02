import dash
from dash import dash_table
from dash import dcc # dash core components
from dash import html
from dash.dependencies import Input, Output, State
import pandas as pd

df = pd.read_csv('https://bit.ly/elements-periodic-table')

app = dash.Dash(__name__)

def identity(x): return x

pivot = df.pivot_table(
  index='Period',
  columns='Group', 
  values='Element',
  aggfunc=identity,
)

app.layout = html.Div([
    dcc.Dropdown(
        id = 'table-values-dropdown',
        options=[

            
        ]



    ),

    html.Div(dash_table.DataTable(
        id='table',
        columns=[{"name": str(i), "id": str(i)} for i in pivot.columns], 
        data=pivot.to_dict('records'),

    ))
])



app.run_server(debug=True, host="0.0.0.0")