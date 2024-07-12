# Penguins Streamlit Application

This folder contains the code required to run a streamlit application. The code and steps to launch the application are outlined below. 

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

Save the following code in a file named `app.py`.

```python
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins
```

## Load Data 

The `load_penguins` function from the `palmerpenguins` library loads the dataset into a `pandas` DataFrame.

```python
# load the dataset
penguins = load_penguins()
```

## Build App

This code creates a Streamlit application that displays the Palmer Penguins dataset in a table format. It also includes a scatter plot with a dropdown menu for selecting the X-axis and Y-axis variables among the numeric columns. The scatter plot differentiates the species by color.

**Streamlit UI Elements**:
  - `st.title` sets the title of the app.
    ```python
    # app title
    st.title('Palmer Penguins Dashboard')
    ```
  - `st.write` displays text and the dataset.
    ```python
    # scatter plot
    st.write("### Scatter Plot")
    ```
  - `st.selectbox` creates dropdown menus for selecting variables for the scatter plot.
    ```python
    x_axis = st.selectbox('X-axis Variable', numeric_columns)
    y_axis = st.selectbox('Y-axis Variable', numeric_columns, index=1)
    ```
**Scatter Plot** 
  - The scatter plot is created using Seaborn, a visualization library built on top of Matplotlib.
    ```python
    if x_axis and y_axis:
        fig, ax = plt.subplots()
        sns.scatterplot(data=penguins, x=x_axis, y=y_axis, hue='species', ax=ax)
        st.pyplot(fig)
    ```
**Displaying the Dataset**
  - The `st.dataframe` method displays the dataset in a table format within the Streamlit app.
    ```python
    st.write("### Dataset")
    st.dataframe(penguins)
    ```

The full application code is below: 

```python
# app title
st.title('Palmer Penguins Dashboard')

# numeric columns for scatter plot
numeric_columns = penguins.select_dtypes(include=['float64', 'int64']).columns
# drop year
numeric_columns = numeric_columns.drop('year')

# scatter plot
st.write("### Scatter Plot")
x_axis = st.selectbox('X-axis variable', numeric_columns)
y_axis = st.selectbox('Y-axis variable', numeric_columns, index=1)

if x_axis and y_axis:
    fig, ax = plt.subplots()
    sns.scatterplot(data=penguins, x=x_axis, y=y_axis, hue='species', ax=ax)
    st.pyplot(fig)

# display the dataframe as a table
st.write("### Dataset")
st.dataframe(penguins)

# footer
st.write("Data Source: [palmerpenguins](https://github.com/allisonhorst/palmerpenguins)")
```

## Run the Streamlit application

Open your terminal, navigate to the directory containing `app.py`, and run:

```sh
streamlit run app.py
```




