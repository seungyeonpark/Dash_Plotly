import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import plotly.graph_objects as go

app = dash.Dash()

app.layout = html.Div([
    html.Br(),
    html.Br(),
    html.H2('Radnom Number Input'),

    html.Div(id='bound div',
             children=[
                html.H6('Input Lower Bound',
                        style={'display': 'inline-block'}),

                dcc.Input(id='input lower number',
                          value=0,
                          style={'display': 'inline-block',
                                 'margin': 10,
                                 'width': '10%'}),
                html.H6(id='Input Upper Bound',
                        style={'display': 'inline-block'}),

                dcc.Input(id='input upper number',
                          value=0,
                          style={'display': 'inline-block',
                                 'margin': 10,
                                 'width': '10%'})
             ]),

    html.Div(id='random number div',
             children=[
                 html.H6('Input Random Number',
                         style={'display': 'inline-block'}),
                 dcc.Input(id='input random number',
                           value=0,
                           style={'display': 'inline-block',
                                  'margin': 10,
                                  'width': '8%'})
             ]),

    dcc.Graph(id='graph')
])

@app.callback(Output(component_id='graph', component_property='figure'),
              [Input(component_id='button', component_property='n_clicks')],
              [State('input lower number', 'value'),
               State('input upper number', 'value'),
               State('input random number', 'value')])
def update_graph(n_clicks, input_value1, input_value2, input_value3):
    lower_bound = int(input_value1)
    upper_bound = int(input_value2)
    random_number = int(input_value3)

    random_x = np.random.randint(lower_bound, upper_bound, random_number)
    random_y = np.random.randint(lower_bound, upper_bound, random_number)

    trace = go.Scatter(x=random_x,
                       y=random_y,
                       mode='markers',
                       name='Random Variables')

    layout = go.Layout(title='Random Variables',
                       xaxis={'title': 'Range {} ~ {}'.format(lower_bound, upper_bound)})

    fig = go.Figure(data=trace, layout=layout)

    return fig

if __name__ == '__main__':
    app.run_server()
