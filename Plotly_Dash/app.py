import numpy as np
import dash
import plotly.graph_objects as go
import plotly.express as px

df_iris = px.data.iris()

app = dash.Dash(__name__)

app.layout = dash.html.Div(children=[
    dash.dcc.Dropdown(id='column_dd', options=df_iris.columns),
    dash.dcc.Graph(id='bar')
])

@dash.callback(
    dash.Output(component_id='bar', component_property='figure'),
    dash.Input(component_id='column_dd', component_property='value')
)
def update_bar(col):
    df_fig = df_iris.copy()
    if col:
        x = col
    else:
        x = 'species'
    df_bar = df_fig.groupby(x)\
        .agg(count=(x, 'count'))\
        .reset_index()
    # Examine the printed dictionary
    # Create a figure
    fig = go.Figure()
    # Update the type
    fig.add_trace(go.Bar(
        x=df_bar[x],
        y=df_bar['count']
    ))
    # # Update the title text
    fig.update_layout({
        'title':{'text':f'Count of {x}'},
        'xaxis':{'title':f'{x}'},
        'yaxis':{'title':'count'}
    })
    
    return fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
