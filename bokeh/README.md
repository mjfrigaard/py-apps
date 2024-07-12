# Bokeh penguins app

The Python code below constructs an interactive Bokeh application with dropdowns to select x and y variables for a scatter plot and a data table displaying the dataset. 

## Set up virtual environment 

Set up a Python virtual environment using `venv`

```sh
python -m venv .venv
```

Activate the environment: 

```sh
source .venv/bin/activate
```

Install the requirements 

```sh
pip install -r requirements.txt
```

## Import Libraries

Load the necessary libraries: `pandas` is for data manipulation, `bokeh` is for interactive visualizations, and `palmerpenguins` to load the penguin dataset.

```python
import pandas as pd
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, DataTable, TableColumn, NumberFormatter, Select
from bokeh.plotting import figure, curdoc
from palmerpenguins import load_penguins
```

## Load the penguins dataset

The penguin dataset is loaded into a DataFrame and remove missing data.

```python
df = load_penguins()
df = df.dropna()
```


A `ColumnDataSource` is created from the DataFrame, which is used by Bokeh for efficient data handling.

```python
source = ColumnDataSource(df)
```


## Define Numeric Columns

A list of numeric columns is defined for use in the scatter plot.

```python
numeric_columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
```

## Create Select Widgets

Created two dropdown widgets for selecting x and y axes variables.

```python
x_select = Select(title="X Axis", value="bill_length_mm", options=numeric_columns)
y_select = Select(title="Y Axis", value="bill_depth_mm", options=numeric_columns)
```

## Scatter Plot Initialization

A scatter plot figure is created and initialized with default axis labels and data.

```python
scatter_plot = figure(title="Scatter Plot",
                      x_axis_label='Bill Length (mm)',
                      y_axis_label='Bill Depth (mm)')
scatter_plot.scatter(x='bill_length_mm', y='bill_depth_mm', source=source, size=10)
```

## Update Plot Function

This function updates the scatter plot when a new variable is selected for the x or y axis. It changes axis labels and re-renders the plot with new data.

```python
def update_plot(attr, old, new):
    x = x_select.value
    y = y_select.value
    scatter_plot.xaxis.axis_label = x.replace('_', ' ').title()
    scatter_plot.yaxis.axis_label = y.replace('_', ' ').title()
    scatter_plot.renderers = []  # Clear existing renderers
    scatter_plot.scatter(x=x, y=y, source=source, size=10)

x_select.on_change("value", update_plot)
y_select.on_change("value", update_plot)
```

## Define Columns for DataTable

Define columns and their formatters for the data table to be displayed, then create a DataTable widget that displays the data.

```python
columns = [
    TableColumn(field="species", title="Species"),
    TableColumn(field="island", title="Island"),
    TableColumn(field="bill_length_mm", title="Bill Length (mm)", formatter=NumberFormatter(format="0.0")),
    TableColumn(field="bill_depth_mm", title="Bill Depth (mm)", formatter=NumberFormatter(format="0.0")),
    TableColumn(field="flipper_length_mm", title="Flipper Length (mm)", formatter=NumberFormatter(format="0")),
    TableColumn(field="body_mass_g", title="Body Mass (g)", formatter=NumberFormatter(format="0")),
    TableColumn(field="sex", title="Sex"),
    TableColumn(field="year", title="Year", formatter=NumberFormatter(format="0"))
]
data_table = DataTable(source=source, columns=columns, width=800)
```


## Layout and Add to Document

The layout is defined and added to the current document for rendering.

```python
layout = column(row(x_select, y_select), scatter_plot, data_table)
curdoc().add_root(layout)
```

### Running the Code

To run this code, save ` main.py` and use the following command:

```python
bokeh serve --show main.py
```

