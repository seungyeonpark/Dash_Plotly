import pandas as pd
import plotly.graph_objs as go
import numpy as np

df = pd.read_excel('../df_etf.xlsx', index_col=0)
df_copy = df.copy()

condition_tiger = [
    df_copy.columns[i] for i in range(df_copy.shape[1]) if 'TIGER' in df_copy.columns[i]
]

df_copy_tiger = df_copy.loc[:, condition_tiger]

date = '2022-02-14'

oneday_return = np.round(df_copy_tiger.pct_change(periods=1) * 100, 1)
oneday_return_sample = oneday_return.loc[date]
return_std = np.round(np.std(oneday_return.tail(180)), 1)

df_tiger_return = pd.DataFrame(
    {'1d Return': oneday_return_sample, 'Return Std': return_std})
df_tiger_return = df_tiger_return.sort_values('1d Return', ascending=False)
df_tiger_return_sample = df_tiger_return.iloc[:10]

data = [go.Scatter(x=df_tiger_return_sample.index,
                   y=df_tiger_return_sample['1d Return'],
                   mode='markers',
                   text=df_tiger_return_sample['Return Std'],
                   marker=dict(size=df_tiger_return_sample['Return Std'] * 30))]

layout = go.Layout(title='TIGER ETF Return {}'.format(date))
fig = go.Figure(data=data, layout=layout)

fig.show()
