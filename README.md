# Plotly
### Overview
The plotly Python package exists to create, manipulate and render graphical figures (i.e. charts, plots, maps and diagrams) represented by data structures also referred to as figures. The rendering process uses the Plotly.js JavaScript library under the hood although Python developers using this module very rarely need to interact with the Javascript library directly, if ever. Figures can be represented in Python either as dicts or as instances of the plotly.graph_objects.Figure class, and are serialized as text in JavaScript Object Notation (JSON) before being passed to Plotly.js.

### Figure reference
https://plotly.com/python/reference/index/

### API reference
https://plotly.com/python-api-reference/

# Dash
### Overview
Dash is an open-source web application framework that allows you to build web applications using only Python. It is built on top of Flask, Plotly.js, and React.js, and provides an intuitive and user-friendly interface for building interactive web applications.

### Installing Dash
``` python
pip install dash
```

### Importing the Required Libraries
``` python
import dash
import dash_core_components as dcc
import dash_html_components as html
```

### Creating the Application Object
``` python
app = dash.Dash(__name__)
```

### Defining the Application Layout
The layout is defined using HTML and CSS, and can include various components such as text, graphs, and input fields.
``` python
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='Dash: A web application framework for Python.'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
```

### Running the Application
``` python
if __name__ == '__main__':
    app.run_server(debug=True)
```

### Callbacks
The @app.callback decorator is used to define a callback function that will be executed when an input component's value changes. The callback function takes the current values of the input components as its arguments, and returns the new values of the output components.
``` python
@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_output_div(input_value):
    return f'You entered: {input_value}'
```

### State
The State object does not trigger the callback when its value changes. Instead, the State object is used to pass the current state of a component to a callback function, where it can be used to perform further computations or update other components.
``` python
@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='button', component_property='n_clicks')],
    [State(component_id='input', component_property='value')]
)
def update_output_div(n_clicks, input_value):
    return f'You clicked the button {n_clicks} times and entered: {input_value}'
```

### API reference
https://dash.plotly.com/reference