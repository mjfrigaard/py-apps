# Bokeh penguins app

The Python code below constructs an interactive Bokeh application with dropdowns to select x and y variables for a scatter plot and a data table displaying the dataset. 

## Import Libraries

```python
import pandas as pd
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, DataTable, TableColumn, NumberFormatter, Select
from bokeh.plotting import figure, curdoc
from palmerpenguins import load_penguins
```

**Explanation**: Here, various libraries are imported. `pandas` is for data manipulation, `bokeh` is for interactive visualizations, and `palmerpenguins` to load the penguin dataset.

**R Comparison**: Similar to R, where you might use `library(dplyr)` for data manipulation and `library(ggplot2)` for visualizations. For interactive visualizations, you might use `library(shiny)`.

## Load the penguins dataset

```python
df = load_penguins()
```

**Explanation**: The penguin dataset is loaded into a DataFrame.

**R Comparison**: In R, you might load the dataset using `data("penguins", package = "palmerpenguins")`.

## Drop missing data

```python
df = df.dropna()
```

**Explanation**: Missing data is removed from the DataFrame.

**R Comparison**: In R, this is done using `df <- na.omit(df)`.

## Create ColumnDataSource

```python
source = ColumnDataSource(df)
```

**Explanation**: A `ColumnDataSource` is created from the DataFrame, which is used by Bokeh for efficient data handling.

**R Comparison**: In R, you might prepare a dataset for plotting directly without this intermediary step, as `ggplot2` handles data frames natively.

## Define Numeric Columns

```python
numeric_columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
```
**Explanation**: A list of numeric columns is defined for use in the scatter plot.

**R Comparison**: In R, you'd also define columns of interest, possibly using `colnames()` or `select()` from `dplyr`.

## Create Select Widgets

```python
x_select = Select(title="X Axis", value="bill_length_mm", options=numeric_columns)
y_select = Select(title="Y Axis", value="bill_depth_mm", options=numeric_columns)
```

**Explanation**: Two dropdown widgets are created for selecting x and y axes variables.

**R Comparison**: In `shiny`, you would use `selectInput()` for similar dropdown menus.

## Scatter Plot Initialization

```python
scatter_plot = figure(title="Scatter Plot",
                      x_axis_label='Bill Length (mm)',
                      y_axis_label='Bill Depth (mm)')
scatter_plot.scatter(x='bill_length_mm', y='bill_depth_mm', source=source, size=10)
```

**Explanation**: A scatter plot figure is created and initialized with default axis labels and data.

**R Comparison**: In `ggplot2`, this would look like `ggplot(df, aes(x = bill_length_mm, y = bill_depth_mm)) + geom_point()`.

## Update Plot Function

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

**Explanation**: This function updates the scatter plot when a new variable is selected for the x or y axis. It changes axis labels and re-renders the plot with new data.

**R Comparison**: In `shiny`, you would use `observeEvent()` or `reactive()` to update plots dynamically.

## Define Columns for DataTable

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
```

**Explanation**: Defines columns and their formatters for the data table to be displayed.

**R Comparison**: In `DT` package of R, you would define columns using `datatable()` and specify options for formatting.

## Create DataTable

```python
data_table = DataTable(source=source, columns=columns, width=800)
```

**Explanation**: Creates a DataTable widget that displays the data.

**R Comparison**: This is similar to using `datatable(df)` from the `DT` package in R.

## Layout and Add to Document

```python
layout = column(row(x_select, y_select), scatter_plot, data_table)
curdoc().add_root(layout)
```

**Explanation**: The layout is defined and added to the current document for rendering.

**R Comparison**: In `shiny`, you would use `fluidPage()`, `sidebarLayout()`, `mainPanel()`, etc., to arrange UI components.

### Running the Code

To run this code, save ` main.py` and use the following command:

```python
bokeh serve --show main.py
```

**Explanation**: Instructions on how to run the script using Bokeh server.

**R Comparison**: In R, you would run a `shiny` app using `shinyApp(ui, server)` and the `runApp()` function.

