import numpy as np
import dash
import plotly.express as px

df = px.data.gapminder()
logo_link = 'https://avatars.githubusercontent.com/u/44514389?v=4'

df_bar = df.groupby(by=['continent', 'country'])\
    .agg(avgGDPCap=('gdpPercap', np.average))\
    .sort_values(by='avgGDPCap', ascending=False)\
    .reset_index()
top_country = df_bar.loc[0]['country']
fig_bar = px.bar(data_frame=df_bar,
    x='avgGDPCap', y='country', color='continent')
fig_bar.update_layout({
    'yaxis':{'dtick':5, 'categoryorder':'total ascending'},
    'paper_bgcolor':'rgb(224, 255, 252)'
})

app = dash.Dash(__name__)
app.layout = dash.html.Div(children=[
    dash.html.Img(src=logo_link,
        style={'width':'50px', 'height':'50px'}),
    dash.html.H1("Avg GDP/Cap by country"),
    dash.html.Div(dash.dcc.Graph(figure=fig_bar,
        style={'width':'500px', 'height':'500px', 'margin':'auto'})),
    dash.html.Br(),
    dash.html.Span(children=[
        "The top country is: ",
        dash.html.B(top_country),
        dash.html.Br(),
        dash.html.I('Copyright E-Com Inc',
            style={'background-color':'lightgrey'})
    ])
    ], style={'text-align':'center', 'font-size':22,
        'background-color':'rgb(224, 255, 252)'}
)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
