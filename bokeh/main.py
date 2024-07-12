import pandas as pd
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, DataTable, TableColumn, NumberFormatter, Select
from bokeh.plotting import figure, curdoc
from palmerpenguins import load_penguins

# load the penguins dataset
df = load_penguins()

# drop missing data 
df = df.dropna()

# create ColumnDataSource
source = ColumnDataSource(df)

# numeric columns
numeric_columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']

# create select widgets for x and y axis
x_select = Select(title="X Axis", value="bill_length_mm", options=numeric_columns)
y_select = Select(title="Y Axis", value="bill_depth_mm", options=numeric_columns)

# scatter plot comparing selected variables
scatter_plot = figure(title="Scatter Plot",
                      x_axis_label='Bill Length (mm)',
                      y_axis_label='Bill Depth (mm)')

scatter_plot.scatter(x='bill_length_mm', y='bill_depth_mm', source=source, size=10)

def update_plot(attr, old, new):
    x = x_select.value
    y = y_select.value
    scatter_plot.xaxis.axis_label = x.replace('_', ' ').title()
    scatter_plot.yaxis.axis_label = y.replace('_', ' ').title()
    scatter_plot.renderers = []  # Clear existing renderers
    scatter_plot.scatter(x=x, y=y, source=source, size=10)

x_select.on_change("value", update_plot)
y_select.on_change("value", update_plot)

# define columns 
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

# create DataTable
data_table = DataTable(source=source, columns=columns, width=800)

# Layout
layout = column(row(x_select, y_select), scatter_plot, data_table)

# add layout to curdoc
curdoc().add_root(layout)