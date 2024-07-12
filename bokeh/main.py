import pandas as pd
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, DataTable, TableColumn, NumberFormatter
from bokeh.plotting import figure, curdoc
from palmerpenguins import load_penguins

# Load the penguins dataset
df = load_penguins()

# Handle missing data by dropping rows with any missing values
df = df.dropna()

# Create ColumnDataSource
source = ColumnDataSource(df)

# Scatter plot comparing bill length and bill depth
scatter_plot = figure(title="Bill Length vs Bill Depth",
                      x_axis_label='Bill Length (mm)',
                      y_axis_label='Bill Depth (mm)')

scatter_plot.scatter(x='bill_length_mm', y='bill_depth_mm', source=source, size=10)

# Define columns for DataTable
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

# Create DataTable
data_table = DataTable(source=source, columns=columns, width=800)

# Layout
layout = column(scatter_plot, data_table)

# Add layout to curdoc
curdoc().add_root(layout)

# To run this code, save it to a file (e.g., main.py) and use the command:
# bokeh serve --show main.py
