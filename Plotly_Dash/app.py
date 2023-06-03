import numpy as np
import dash
import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__)
app.layout = dash.html.Div([
    dash.dcc.Graph(
        figure=go.Figure({
            'data': [{
                'type': 'bar',
                'x': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday', 'Sunday'],
                'y': [28, 27, 25, 31, 32, 35, 36]
            }],
            'layout': {
                'title': {
                    'text': 'Temperatures of the week',
                    'x': 0.5,
                    'font': {
                        'color': 'red',
                        'size': 15
                    }
                }
            }
        })
    ),
    dash.dcc.Graph(
        figure=px.bar(
            data_frame=px.data.tips()\
                .groupby(by='day').agg(avg_tip=('tip', np.average))\
                .reset_index(),
            x='day', y='avg_tip', color='avg_tip'
        )
    )
])
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
