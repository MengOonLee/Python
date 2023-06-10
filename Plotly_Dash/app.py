import numpy as np
from datetime import datetime
import dash
import plotly.express as px

logo_link = 'https://avatars.githubusercontent.com/u/44514389?v=4'

df = px.data.gapminder()
country1, lifeExp1 = df.iloc[np.argmax(df['lifeExp'])]\
    [['country', 'lifeExp']]
country2, lifeExp2 = df.iloc[np.argmin(df['lifeExp'])]\
    [['country', 'lifeExp']]

marker_life_gdp = px.scatter(data_frame=df,
    x='gdpPercap', y='lifeExp', color='continent',
    size='pop', size_max=50, log_x=True,
    range_x=[np.min(df['gdpPercap']),
        np.max(df['gdpPercap'])],
    range_y=[np.min(df['lifeExp'])-10, np.max(df['lifeExp'])+10],
    animation_frame='year', animation_group='country',
    hover_name='country', labels={'gdpPercap':'GDP Per Capital',
        'lifeExp':'Life Expectency', 'pop':'Population'}
)
marker_life_gdp.update_layout(
    hovermode='closest',
    margin={'l':40, 'b':40, 't':10, 'r':10},
    template='plotly_dark'
)

map_gdp = px.choropleth(data_frame=df, locations='iso_alpha',
    color='gdpPercap', hover_name='country',
    range_color=(np.min(df['gdpPercap']), np.max(df['gdpPercap'])),
    animation_frame='year')
map_gdp.update_layout(
    template='plotly_dark')

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
    dash.html.H1("Continent Life Expectency, GDP per Capital"),
    dash.html.Div(children=[
        dash.dcc.Graph(id='map_gdp', figure=map_gdp),
        dash.dcc.Graph(id='marker_life_gdp', figure=marker_life_gdp),
        dash.html.Span(children=[
            "The top & last country by life expectency are:",
            dash.html.Ol(children=[
                dash.html.Li(children=[
                    country1, ", ", lifeExp1, " years"
                ]),
                dash.html.Li(children=[
                    country2, ", ", lifeExp2, " years"
                ])
            ], style={'width':'35%', 'margin':'auto'})
        ])
    ], style={'width':'80%', 'margin':'auto'}),
], style={'text-align':'center', 'font-size':18,
    'background-color':'black', 'color':'white'})

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
