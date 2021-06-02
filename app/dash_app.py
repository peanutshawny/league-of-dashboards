import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from dash_data import winrate_df, pickrate_df, damage_df

app = dash.Dash(__name__)

# app layout
app.layout = html.Div([

    html.H1('League of Legends Dashboard', style={'text-align': 'center'}),

    dcc.Input(
        id='input_champ',
        type='text',
        placeholder='Input Champion'
    ),

    html.Div(id='winrate_container', children=[]),
    html.Br(),

    dcc.Graph(id='winrate_pie_chart', figure={})

])


# callbacks to connect plotly graphs with dash components
@app.callback(
    Output(component_id='winrate_container', component_property='children'),
    Input(component_id='input_champ', component_property='value')
)
def winrate_pie_chart(champ_slctd):
    container = f'The champion chosen by user was: {champ_slctd}'

    winrate_dff = winrate_df.copy()
    winrate_dff = winrate_dff[winrate_dff['champion'] == champ_slctd]

    return container


if __name__ == '__main__':
    app.run_server(debug=True)
