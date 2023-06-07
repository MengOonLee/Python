import numpy as np
import dash
import plotly.express as px

df = px.data.gapminder()
logo_link = 'https://avatars.githubusercontent.com/u/44514389?v=4'

df_line = df.groupby(by=['continent', 'year'])\
    .agg(avgGDPCap=('gdpPercap', np.average))\
    .reset_index()\
    .sort_values(by=['continent', 'year'])
fig_line = px.line(data_frame=df_line,
    x='year', y='avgGDPCap', color='continent')
fig_line.update_layout({'paper_bgcolor':'rgb(224, 255, 252)'})

df_bar = df.groupby(by='continent')\
    .agg(avgGDPCap=('gdpPercap', np.average))\
    .reset_index()\
    .sort_values(by='avgGDPCap', ascending=False)
fig_bar = px.bar(data_frame=df_bar,
    x='avgGDPCap', y='continent', color='continent',
    orientation='h')
fig_bar.update_layout({
    'yaxis':{'dtick':5, 'categoryorder':'total ascending'},
    'paper_bgcolor':'rgb(224, 255, 252)'})

app = dash.Dash(__name__)
app.layout = dash.html.Div(children=[
    dash.html.Div(children=[
        dash.html.Img(src=logo_link,
            style={'width':'50px', 'height':'50px',
                'display':'inline-block', 'margin':'25px'}),
        dash.html.H1(children=['Avg GDP/Cap Dashboard'],
            style={'display':'inline-block'}),
        dash.html.Img(src=logo_link,
            style={'width':'50px', 'height':'50px',
                'display':'inline-block', 'margin':'25px'})]),
    dash.html.Div(dash.dcc.Graph(figure=fig_line),
        style={'width':'500px', 'display':'inline-block',
            'margin':'5px'}),
    dash.html.Div(dash.dcc.Graph(figure=fig_bar),
        style={'width':'350px', 'display':'inline-block',
            'margin':'5px'}),
    dash.html.H3(f"The largest GDP/Cap was {df['gdpPercap'].max()}")
    ], style={'text-align':'center', 'font-size':22,
        'background-color':'rgb(224, 255, 252)'})

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
