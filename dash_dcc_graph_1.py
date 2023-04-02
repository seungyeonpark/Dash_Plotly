import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

app = dash.Dash()

colors = {'background': '#111111', 'text': '#7FDBFF'}

x1_values = [1, 2, 3]
y1_values = [4, 1, 2]
x2_values = [1, 2, 3]
y2_values = [2, 4, 5]

trace1 = go.Bar(x=x1_values,
                y=y1_values,
                name='SF')

trace2 = go.Bar(x=x2_values,
                y=y2_values,
                name='Montreal')

data = [trace1, trace2]

layout = go.Layout(title='Dash Data Visualization',
                   plot_bgcolor=colors['background'],
                   paper_bgcolor=colors['background'],
                   font={'color': colors['text']})

fig = go.Figure(data=data, layout=layout)

app.layout = html.Div(
    [
        html.H1(id='H1',
                children='Hello Dash',
                style={'textAlign': 'center',
                       'color': colors['text']}
                ),
        html.H3(id='H3',
                children='Dash: A web application framwork for Python.',
                style={'textAlign': 'center',
                       'color': colors['text']}),

        dcc.Graph(id='example-graph',
                  figure=fig)
    ],
    style={'backgroundColor': colors['background']}
)

if __name__ == '__main__':
    app.run_server()
