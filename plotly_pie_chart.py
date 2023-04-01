import numpy as np
import plotly.graph_objs as go
import pandas as pd

np.random.seed(1)

random_x = np.random.randint(0, 100, 5)
idx = ['A', 'B', 'C', 'D', 'E']

df = pd.DataFrame(random_x)
df.index = idx
df.columns = ['Random Variable']

trace = go.Pie(labels=df.index,
               values=df['Random Variable'])

layout = go.Layout(title='Pie Chart')

fig = go.Figure(trace, layout)

fig.show()
