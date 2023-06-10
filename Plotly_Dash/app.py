import numpy as np
from datetime import datetime
import dash
import plotly.express as px
import plotly.graph_objects as go

logo_link = 'https://avatars.githubusercontent.com/u/44514389?v=4'

df = px.data.gapminder()
country1, lifeExp1 = df.iloc[np.argmax(df['lifeExp'])]\
    [['country', 'lifeExp']]
country2, lifeExp2 = df.iloc[np.argmin(df['lifeExp'])]\
    [['country', 'lifeExp']]

marker_life_gdp = go.Figure()
for c in df['continent'].unique():
    mask = df['continent']==c
    marker_life_gdp.add_trace(go.Scatter(
        x=df[mask]['gdpPercap'],
        y=df[mask]['lifeExp'],
        name=c,
        text=df[mask]['country'],
        mode='markers',
        marker={'size':15, 'line':{'width':0.5, 'color':'white'}},
        opacity=0.8
    ))
marker_life_gdp.update_layout(
    xaxis={'type':'log', 'title':'GDP per Capita'},
    yaxis={'title':'Life Expectancy'},
    legend={'x':0, 'y':1},
    hovermode='closest',
    margin={'l':40, 'b':40, 't':10, 'r':10},
    paper_bgcolor='black',
    font={'color':'white'}
)
    
app = dash.Dash(__name__)
app.layout = dash.html.Div(children=[
    dash.html.Img(src=logo_link,
        style={'width':'5%', 'height':'5%',
            'display':'inline-block', 'margin':'1%'}),
    dash.html.Span(children=[
        dash.html.Br(),
        f"Prepared: {datetime.now().date()}",
        dash.html.Br(),
        " by ", dash.html.B("Meng Oon Lee, "),
        dash.html.Br(),
        dash.html.I("Data Scientist")
    ], style={'display':'inline-block'}),
    dash.html.Img(src=logo_link,
        style={'width':'5%', 'height':'5%',
            'display':'inline-block', 'margin':'1%'}),
    dash.html.H1("Continent Life Expectancy, GDP per Capita"),
    dash.html.Div(children=[
        dash.dcc.Graph(id='marker_life_gdp', figure=marker_life_gdp),
        dash.html.Span(children=[
            "The top & last country by life expectancy are:",
            dash.html.Ol(children=[
                dash.html.Li(children=[
                    country1, ", ", lifeExp1, " years"
                ]),
                dash.html.Li(children=[
                    country2, ", ", lifeExp2, " years"
                ])
            ], style={'width':'35%', 'margin':'auto'})
        ])
    ], style={'width':'75%', 'margin':'auto'}),
], style={'text-align':'center', 'font-size':18,
    'background-color':'black', 'color':'white'})

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
