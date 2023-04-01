import numpy as np
import plotly.graph_objs as go
import pandas as pd

np.random.seed(2)

salesGrowth = np.round(np.random.random(5) * 100, 1)
opm = np.round(np.random.random(5) * 100, 1)

df = pd.DataFrame({'salesGrowth': salesGrowth, 'OPM': opm})
df.index = ['AAPL', 'MS', 'TSLA', 'MT', 'GOOL']

trace1 = go.Bar(x=df.index,
                y=df['salesGrowth'],
                name='salesGrowth')

trace2 = go.Bar(y=df.index,
                x=df['salesGrowth'],
                name='salesGrowth',
                orientation='h')

trace3 = go.Bar(y=df.index,
                x=df['OPM'],
                name='OPM',
                orientation='h')

data = [trace2, trace3]

layout = go.Layout(title='Company IS')

fig = go.Figure(data=data, layout=layout)

fig.show()
