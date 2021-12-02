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
  aggfunc=identity,)

app.layout = html.Div([
    html.H3(children = 'Remove the default items from the dropdown'),
    html.H3(children = 'and then select three columns,'),
    html.H3(children = 'one each for the index, columns and values:'),
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
        value = ['Period', 'Group', 'Element'],
        multi = True
        
    ),
    html.H3(children = 'After making your selections, click "Update" !'),
    html.Button("Update", id="Update"),
    
    html.Div(dash_table.DataTable(
        id='table',
        columns=[{"name": str(i), "id": str(i)} for i in pivot.columns], 
        data=pivot.to_dict('records'),

    ))
])

@app.callback(
    [Output(component_id = 'table', component_property = 'data'),
    Output(component_id = 'table', component_property = 'columns')],
    State(component_id = 'table-values-dropdown', component_property = 'value'),
    Input(component_id = 'Update', component_property = 'n_clicks'),
)

def update_table(value, n_clicks):
    pivot = df.pivot_table(
        index=value[0],
        columns=value[1], 
        values=value[2],
        aggfunc=identity,)
        
    columns=[{"name": str(i), "id": str(i)} for i in pivot.columns]
    data=pivot.to_dict('records')

    return data, columns

app.run_server(debug=True, host="0.0.0.0")