import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np

app = dash.Dash()

random_x1 = np.random.randint(0, 100, 50)
random_y1 = np.random.randint(0, 100, 50)

trace1 = go.Scatter(x=random_x1,
                    y=random_y1,
                    mode='markers',
                    marker={'size': 12,
                            'color': 'rgb(50,200,153)',
                            'symbol': 'pentagon',
                            'line': {'width': 2}})

layout1 = go.Layout(title='Random Variable Scatter Plot1',
                    xaxis={'title': 'Random X Variables 1'},
                    yaxis={'title': 'Radndom Y Variables 1'})

fig1 = go.Figure(data=trace1, layout=layout1)

random_x2 = np.random.randint(0, 100, 50)
random_y2 = np.random.randint(0, 100, 50)

trace2 = go.Scatter(x=random_x2,
                    y=random_y2,
                    mode='markers',
                    marker={'size': 10,
                            'color': 'rgb(30,150,200)',
                            'line': {'width': 2}})

layout2 = go.Layout(title='Random Variable Scatter Plot2',
                    xaxis={'title': 'Random X Variables 2'},
                    yaxis={'title': 'Radndom Y Variables 2'})

fig2 = go.Figure(data=trace2, layout=layout2)

app.layout = html.Div([
    html.Div(id='Div1', children=[
        dcc.Graph(id='Random Variables Scatter Plot1',
                  figure=fig1)
    ]),

    html.Div(id='Div2', children=[
        dcc.Graph(id='Random Variables Scatter Plot2',
                  figure=fig2)
    ])
])

if __name__ == '__main__':
    app.run_server()
