import numpy as np
import dash
import plotly.express as px

df = px.data.gapminder()

df_line = df.groupby(by=['continent', 'year'])\
    .agg(avgGDPCap=('gdpPercap', np.average))\
    .reset_index()
fig_line = px.line(data_frame=df_line,
    x='year', y='avgGDPCap', color='continent',
    title='Avg GDP/Cap by Year')

df_bar = df.groupby(by='continent')\
    .agg(avgGDPCap=('gdpPercap', np.average))\
    .reset_index()
fig_bar = px.bar(data_frame=df_bar,
    x='avgGDPCap', y='continent', color='continent',
    title='Avg GDP/Cap by Continent', orientation='h')
max_bar = df_bar.iloc[np.argmax(df_bar['avgGDPCap'])]

app = dash.Dash(__name__)
app.layout = dash.html.Div(children=[
    dash.html.H1('Avg GDP/Cap Dashboard'),
    dash.html.Div(dash.dcc.Graph(id='fig_line', figure=fig_line)),
    dash.html.Div(dash.dcc.Graph(id='fig_bar', figure=fig_bar)),
    dash.html.H3(f"The largest continent by avg GDP/Cap is \
        {max_bar['continent']}")
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
