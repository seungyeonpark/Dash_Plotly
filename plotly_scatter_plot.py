import plotly.graph_objs as go
import numpy as np

np.random.seed(1)

random_x = np.random.randint(500, 2000, 100)
random_y = np.random.randint(200, 400, 100)

trace = go.Scatter(x=random_x, y=random_y, mode='markers',
                   marker=dict(size=8, symbol='pentagon', line=dict(width=2)))

layout = go.Layout(title='Layout Title',
                   xaxis={'title': 'Layout1'},
                   yaxis={'title': 'Layout'},
                   hovermode='closest')

fig = go.Figure(data=trace, layout=layout)

fig.show()
