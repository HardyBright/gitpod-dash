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
            {'label': 'AtomicNumber', 'value': 'AtomicNumber'},
            {'label': 'Element', 'value': 'Element'}, 
            {'label': 'Symbol', 'value': 'Symbol'}, 
            {'label': 'AtomicMass', 'value': 'AtomicMass'}, 
            {'label': 'NumberOfNeutrons', 'value': 'NumberOfNeutrons'}, 
            {'label': 'NumberOfProtons', 'value': 'NumberOfProtons'}, 
            {'label': 'NumberOfElectrons', 'value': 'NumberOfElectrons'}, 
            {'label': 'Period', 'value': 'Period'}, 
            {'label': 'Group', 'value': 'Group'}, 
            {'label': 'Phase', 'value': 'Phase'}, 
            {'label': 'Natural', 'value': 'Natural'}, 
            {'label': 'Metal', 'value': 'Metal'}, 
            {'label': 'Nonmetal', 'value': 'Nonmetal'}, 
            {'label': 'Metalloid', 'value': 'Metalloid'}, 
            {'label': 'Type', 'value': 'Type'}, 
            {'label': 'Electronegativity', 'value': 'Electronegativity'}, 
            {'label': 'FirstIonization', 'value': 'FirstIonization'}, 
            {'label': 'Density', 'value': 'Density'}, 
            {'label': 'MeltingPoint', 'value': 'MeltingPoint'}, 
            {'label': 'BoilingPoint', 'value': 'BoilingPoint'}, 
            {'label': 'NumberOfIsotopes', 'value': 'NumberOfIsotopes'}, 
            {'label': 'Discoverer', 'value': 'Discoverer'}, 
            {'label': 'Year', 'value': 'Year'}, 
            {'label': 'SpecificHeat', 'value': 'SpecificHeat'}, 
            {'label': 'NumberOfShells', 'value': 'NumberOfShells'}, 
            {'label': 'NumberOfValence', 'value': 'NumberOfValence'}, 
        ],
        multi = True
        
    ),
    html.Button("OK!", id="OK!"),
    
    html.Div(dash_table.DataTable(
        id='table',
        columns=[{"name": str(i), "id": str(i)} for i in pivot.columns], 
        data=pivot.to_dict('records'),

    ))
])



app.run_server(debug=True, host="0.0.0.0")