import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label('DropDown'),
    html.Div(id='DropDown_Div',
             children=[
                 dcc.Dropdown(
                     options=[
                         {'label': '삼성전자', 'value': '002380'},
                         {'label': '카카오', 'value': '035720'},
                         {'label': 'SK하이닉스', 'value': '000660'},
                         {'label': 'NAVER', 'value': '035420'}
                     ],
                     placeholder='종목을 선택해주세요',
                     multi=True
                 )
             ], style={'width': '50%'})
])

if __name__ == '__main__':
    app.run_server()
