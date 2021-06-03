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

    html.Div([

        # first pie chart for winrates
        html.Div([

            dcc.Input(
                id='input_champ',
                type='text',
                placeholder='Input Champion',
                debounce=True
            ),

            html.Div(id='winrate_container', children=[]),
            html.Br(),

            dcc.Graph(id='winrate_pie_chart', figure={})

        ], className='six columns'),

        # second pie chart
        html.Div([

            dcc.Graph(id='pickrate_pie_chart', figure={})

        ], className='six columns')

    ], className='row')

])

# css stylesheet - find out why this doesn't work
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# callbacks to connect plotly graphs with dash components
@app.callback(
    Output(component_id='winrate_container', component_property='children'),
    Output(component_id='winrate_pie_chart', component_property='figure'),
    Input(component_id='input_champ', component_property='value')
)
def winrate_pie_chart(champ_slctd):
    container = f'The champion last chosen by user was: {champ_slctd}'

    winrate_dff = winrate_df.copy()

    fig = px.pie(
        winrate_dff,
        names=winrate_dff.index,
        values=winrate_dff[champ_slctd],
        hole=.3,
        template='presentation'
    )

    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)
