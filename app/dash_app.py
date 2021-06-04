import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from dash_data import winrate_df, pickrate_df, damage_df

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app layout
app.layout = html.Div([

    html.H1('League of Legends Dashboard', style={'text-align': 'center'}),

    html.Div([

        # first pie chart for winrates
        html.Div([

            html.Div([

                dcc.Input(
                    id='input_champ',
                    type='text',
                    placeholder='Input Champion',
                    debounce=True
                )

            ], style={'display': 'flex', 'justifyContent': 'center'}),

            html.Div(),
            html.Br(),

            dcc.Graph(id='winrate_pie_chart', figure={})

        ], className='six columns'),

        # second pie chart
        html.Div([

            dcc.Graph(id='pickrate_pie_chart', figure={})

        ], className='six columns')

    ], className='row')

])


# callbacks to connect plotly graphs with dash components
@app.callback(
    Output(component_id='winrate_container', component_property='children'),
    Output(component_id='winrate_pie_chart', component_property='figure'),
    Input(component_id='input_champ', component_property='value')
)
def winrate_pie_chart(champ_slctd):
    container = f'The champion last chosen by user was: {champ_slctd}'

    winrate_dff = winrate_df.copy()

    winrate_fig = px.pie(
        winrate_dff,
        names=winrate_dff.index,
        values=winrate_dff[champ_slctd],
        hole=.3,
        template='presentation'
    )

    return container, winrate_fig


if __name__ == '__main__':
    app.run_server(debug=True)
