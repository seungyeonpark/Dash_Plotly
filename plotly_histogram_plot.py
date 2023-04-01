import numpy as np
import plotly.graph_objs as go

random_x = np.random.randint(0, 100, 100)

trace1 = go.Histogram(x=random_x, nbinsx=100)

layout = go.Layout(title='Histogram of RandomVariable')

fig = go.Figure(data=trace1, layout=layout)

fig.show()
