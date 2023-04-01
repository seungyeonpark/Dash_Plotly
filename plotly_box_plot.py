import numpy as np
import plotly.graph_objs as go

random_x1 = np.random.randint(0, 100, 100)
random_x2 = np.random.randint(50, 150, 100)

trace1 = go.Box(y=random_x1, name='random_x1', boxpoints='all')
trace2 = go.Box(y=random_x2, name='random_x2')

data = [trace1, trace2]

layout = go.Layout(title='Random Varaible')

fig = go.Figure(data=data, layout=layout)

fig.show()
