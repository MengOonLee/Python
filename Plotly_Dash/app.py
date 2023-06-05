import numpy as np
import datetime
import dash
import plotly.express as px

df = px.data.gapminder()
logo_link = 'https://avatars.githubusercontent.com/u/44514389?v=4'

df_bar = df.groupby(by=['continent', 'country'])\
    .agg(avgGDPCap=('gdpPercap', np.average))\
    .sort_values(by='avgGDPCap', ascending=False)\
    .reset_index()
country1, avgGDPCap1 = df_bar.loc[0].tolist()[1:3]
country2, avgGDPCap2 = df_bar.loc[1].tolist()[1:3]
fig_bar = px.bar(data_frame=df_bar,
    x='avgGDPCap', y='country', color='continent')
fig_bar.update_layout({
    'yaxis':{'dtick':5, 'categoryorder':'sum ascending'}
})

app = dash.Dash(__name__)
app.layout = dash.html.Div(children=[
    dash.html.Img(src=logo_link,
        style={'width':'50px', 'height':'50px'}
    ),
    dash.html.Span(children=[
        dash.html.Br(),
        f"Prepared: {datetime.datetime.now().date()}",
        dash.html.Br(),
        " by ", dash.html.B("Meng Oon Lee, "),
        dash.html.Br(),
        dash.html.I("Data Scientist")
    ]),
    dash.html.H1("Avg GDP/Cap by Country"),
    dash.html.Div(dash.dcc.Graph(figure=fig_bar)),
    dash.html.Span(children=[
        "The top 2 avg GDP/Cap countries are:",
        dash.html.Ol(children=[
            dash.html.Li(children=[
                country1, " with ", avgGDPCap1, " avg GDP/Cap"
            ]),
            dash.html.Li(children=[
                country2, " with ", avgGDPCap2, " avg GDP/Cap"
            ])
        ], style={'width':'350px', 'margin':'auto'})
    ])
], style={'text-align':'center', 'font-size':22})

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
