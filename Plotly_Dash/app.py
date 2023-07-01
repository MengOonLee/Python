import dash
import plotly.express as px
import pandas as pd

logo_link = 'https://avatars.githubusercontent.com/u/44514389?v=4'

ecom_sales = pd.read_csv('./Data/ecom_sales.csv',
    parse_dates=['InvoiceDate'])
ecom_sales['Year-Month'] = ecom_sales['InvoiceDate']\
    .dt.to_period('M').astype(str)
ecom_sales['OrderValue'] = ecom_sales['Quantity']\
    *ecom_sales['UnitPrice']

ecom_bar = ecom_sales.groupby('Country')['OrderValue']\
    .agg('sum').reset_index(name='Total Sales ($)')\
    .sort_values(by='Total Sales ($)', ascending=False)
top_country = ecom_bar.iloc[0]['Country']            
bar_fig_country = px.bar(data_frame=ecom_bar,
    x='Total Sales ($)', y='Country', color='Country',
    color_discrete_map={'United Kingdom':'lightblue',
        'Germany':'orange', 'France':'darkblue', 
        'Australia':'green', 'Hong Kong':'red'})

app = dash.Dash(__name__)

app.layout = dash.html.Div(children=[
    # Add the company logo
    dash.html.Img(src=logo_link),
    dash.html.H1('Sales by Country'),
    dash.html.Div(dash.dcc.Graph(figure=bar_fig_country), 
        style={'width':'750px', 'margin':'auto'}),
    # Add an overall text-containing component
    dash.html.Span(children=[
        # Add the top country text
        'This year, the most sales came from: ', 
        dash.html.B(top_country),
        # Italicize copyright notice
        dash.html.I(' Copyright E-Com INC')])
], style={'text-align':'center', 'font-size':22})

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
