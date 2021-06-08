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

    dcc.Input(
        id='input_champ',
        type='text',
        placeholder='Input Champion',
        debounce=True
    ),

    html.Div([

        # first pie chart for winrates
        html.Div([

            html.H2('Champion Win Rate', style={'display': 'flex', 'justifyContent': 'center'}),

            dcc.Graph(id='winrate_pie_chart', figure={})

        ], className='six columns'),

        # second pie chart
        html.Div([

            html.H2('Champion Pick Rate', style={'display': 'flex', 'justifyContent': 'center'}),

            dcc.Graph(id='pickrate_pie_chart', figure={})

        ], className='six columns'),

    ], className='row'),

    html.Div([

        html.H2('Champion Damage Dealt', style={'display': 'flex', 'justifyContent': 'center'}),

        dcc.Graph(id='damage_bar_chart', figure={})

    ]),

])


# callbacks to connect plotly graphs with dash components
@app.callback(
    Output(component_id='winrate_pie_chart', component_property='figure'),
    Output(component_id='pickrate_pie_chart', component_property='figure'),
    Output(component_id='damage_bar_chart', component_property='figure'),
    Input(component_id='input_champ', component_property='value')
)
def graphs(champ_slctd):

    winrate_dff = winrate_df.copy()
    pickrate_dff = pickrate_df.copy()

    # winrate pie chart
    winrate_fig = px.pie(
        winrate_dff,
        names=winrate_dff.index,
        values=winrate_dff[champ_slctd],
        hole=.3,
        template='presentation'
    )

    # pickrate pie chart
    pickrate_fig = px.pie(
        pickrate_dff,
        names=pickrate_dff.index,
        values=pickrate_dff[champ_slctd],
        hole=.3,
        template='presentation'
    )
    # damage dealt bar chart
    dmg_fig = px.bar(damage_df,
                     x='champion',
                     y='avg_damage_per_game'
    )

    return winrate_fig, pickrate_fig, dmg_fig


if __name__ == '__main__':
    app.run_server(debug=True)
