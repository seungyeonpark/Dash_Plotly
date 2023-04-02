import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_excel('df_etf.xlsx')
df_copy = df.copy()

app = dash.Dash()

kind = 'KODEX'

condition_kodex = [df_copy.columns[i] for i in range(
    df_copy.shape[1]) if 'KODEX' in df_copy.columns[i]]

df_copy_kodex = df_copy.loc[:, condition_kodex]

app.layout = html.Div([
    html.Label('ETF DropDown'),
    html.Div(id='DropDwon Div',
             children=[
                 dcc.Dropdown(
                     options=[
                         {'label': i, 'value': i} for i in df_copy_kodex.columns
                     ],
                     placeholder='Select KODEX ETF ..',
                     multi=True
                 )
             ])
])


if __name__ == '__main__':
    app.run_server()
