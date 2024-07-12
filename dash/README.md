# Penguins-dash

The code sets up a web application to visualize the Palmer Penguins dataset. It uses components for layout and interactivity, similar to Shiny. Reactivity is handled by callback functions that update outputs based on user inputs. Plotting is done using Plotly, similar to `ggplot2` in R.

Below is a breakdown of each part of a Python Dash app. Parallels are drawn to concepts in R, assuming familiarity with Shiny for web applications and `ggplot2` for plotting.

## Importing Libraries 

This section imports necessary libraries:
1. `dash` and submodules are used for building web applications, similar to Shiny.
2. `pandas` is used for data manipulation, similar to `dplyr`.  
3. `plotly.express` for creating plots, akin to `ggplot2`.
4. `dash_bootstrap_components` for styling the app with Bootstrap themes.


```python
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
```


## Loading Data

`read_csv()` from `pandas` reads the CSV file from a URL into a DataFrame. `pd.read_csv` is analogous to `read.csv` or `readr::read_csv()`.

```python
# Load the dataset
url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
df = pd.read_csv(url)
```

## Numeric Columns

Define numeric columns for drop-downs.

```python
# remove the 'year' column 
numerical_columns = [col for col in df.select_dtypes(include=['float64', 'int64']).columns if col != 'year']
```

Similar to using `names()`, `sapply()`, and `is.numeric()` in R.

## Initialize App

`dash.Dash()` creates a Dash app instance with Bootstrap styling.

```python
# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
```

Similar to initializing a Shiny app with `shinyApp()`.

## Utility Function

This function replaces underscores with spaces and capitalizes words. 

```python
def format_label(label):
    return label.replace('_', ' ').title()
```

In R, you would define a similar function using `gsub()` and `tools::toTitleCase()`.

## UI Layout

`app.layout` defines the layout of the web app using Bootstrap components.

1. `dbc.Container`, `dbc.Row`, and `dbc.Col` arrange components in a grid, similar to layout functions in Shiny like `fluidPage()`, `sidebarLayout()`, etc.
    a. `html.H1` creates a header, like `h1()` in Shiny.
2. `dcc.Dropdown` creates dropdown menus for user input, similar to `selectInput()` in Shiny.
3. `dcc.Graph` places a plot in the app, analogous to `plotOutput()` in Shiny.
4. `dash_table.DataTable` displays data in a table, similar to `DT::dataTableOutput()` in R.

```python
# app layout
# app layout
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            html.H1("Palmer Penguins Dashboard"), 
        width=12)
    ),
    dbc.Row(
        html.H3("Inputs")
    ),
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id='x-axis',
                options=[{'label': col, 'value': col} for col in numerical_columns],
                value='bill_length_mm',
                clearable=False
            ), width=3
        ),
        dbc.Col(
            dcc.Dropdown(
                id='y-axis',
                options=[{'label': col, 'value': col} for col in numerical_columns],
                value='bill_depth_mm',
                clearable=False
            ), width=3
        )
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Scatter Plot"),
            dcc.Graph(id='scatter-plot')
        ], width=6),
        dbc.Col([
            html.H3("Table"),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                page_size=10,
                style_table={'overflowX': 'auto'},
                style_cell={
                    'height': 'auto',
                    'minWidth': '140px', 'width': '140px', 'maxWidth': '140px',
                    'whiteSpace': 'normal'
                }
            )
        ], width=6)
    ])
])
```

## Callback for Dynamic Plotting

The callback function updates the scatter plot based on dropdown inputs:

1. The `@app.callback` decorator defines reactive behavior, similar to `observeEvent()` or `reactive()` in Shiny.

2. The function `update_scatter_plot` takes inputs from dropdowns and updates the plot, using `plotly.express` and our `format_label()` utility function to create the scatter plot, similar to using `ggplot2` in R.

```python
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-axis', 'value'),
     Input('y-axis', 'value')]
)
def update_scatter_plot(x_axis, y_axis):
    fig = px.scatter(
        df, x=x_axis, y=y_axis, color='species',
        labels={x_axis: format_label(x_axis), y_axis: format_label(y_axis)},
        title=f'Scatter Plot of {format_label(x_axis)} vs {format_label(y_axis)}'
    )
    return fig
```

## Running the App

`app.run_server()` starts the server to run the app--equivalent to running `shinyApp(ui, server)` in R.

```python
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```

Run the application using: 

``` sh
python app.py
```