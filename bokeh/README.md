# Penguins Bokeh

To rewrite the Bokeh application using the `palmerpenguins` Python package, follow these steps:

1. **Install the necessary packages**

```sh
pip install bokeh pandas palmerpenguins
```

2. **Load the data using the `palmerpenguins` package**.

3. **Create the Bokeh application** to visualize the data.

Here is the complete code:

```python
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

scatter_plot.circle(x='bill_length_mm', y='bill_depth_mm', source=source, size=10)

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
```

### Explanation:
1. **Data Loading**:
    - We used the `palmerpenguins` package to load the dataset with `load_penguins()`.
    - Missing values are handled by dropping rows with any missing values.

2. **Bokeh Visualization**:
    - We created a `ColumnDataSource` from the cleaned DataFrame.
    - A scatter plot comparing bill length and bill depth was created using Bokeh's `figure`.
    - A `DataTable` was defined with columns corresponding to the DataFrame columns.

3. **Layout**:
    - The scatter plot and data table are arranged in a vertical layout using `column`.
    - The layout is added to the Bokeh document (`curdoc`).

4. **Running the Application**:
    - Save the code to a file (e.g., `main.py`).
    - Run the application using the command: `bokeh serve --show main.py`.

This will start a Bokeh server and open a web browser showing the scatter plot and data table with the palmerpenguins dataset.