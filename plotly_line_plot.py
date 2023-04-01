import numpy as np
import plotly.graph_objs as go
import pandas as pd

np.random.seed(1)
random_x = np.random.randint(50, 100, 180)

datetime_index = pd.date_range('2022-05-17', '2022-11-12')

df = pd.DataFrame(random_x)
df.index = datetime_index
df.columns = ['Stock A']

# Single Line
trace = go.Scatterk(x=df.index, y=df['Stock A'], mode='lines', name='Stcok A')
layout = go.Layout(title='Stock A',
                   xaxis={'title': 'datetime'},
                   yaxis={'title': 'Stock A'})

fig = go.Figure(data=trace, layout=layout)

fig.show()
