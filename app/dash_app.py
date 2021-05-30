import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1('League of Legends Dashboard', style={'text-align': 'center'}),

    html.Div(id='output_container', children=[]),
    html.Br()

])

if __name__ == '__main__':
    app.run_server(debug=True)