import numpy as np
import plotly.graph_objs as go

random_matrix = np.random.randint(0, 100, (3, 3))

xaxis = ['A', 'B', 'C']
yaxis = ['1', '2', '3']

trace = go.Heatmap(z=random_matrix, x=xaxis, y=yaxis)

fig = go.Figure(data=trace)

fig.show()
