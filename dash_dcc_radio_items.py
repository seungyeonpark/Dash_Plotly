import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    # Input
    html.Br(),
    html.Label("Date Input"),
    html.Br(),
    dcc.Input(id='Start Date Input',
              value='20200101'),
    dcc.Input(id='End Date Input',
              value='20220331'),
    html.Br(),

    # Radio Items
    html.Label('Radio Items'),
    html.Br(),
    dcc.RadioItems(
        id='RadtioItems',
        options=[
            {'label': 'RSI', 'value': 'RSI'},
            {'label': 'MACD', 'value': 'MACD'}
        ]
    )
])

if __name__ == '__main__':
    app.run_server()
