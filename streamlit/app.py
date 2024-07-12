import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins

# load the dataset
penguins = load_penguins()

# app title
st.title('Palmer Penguins Dashboard')

# numeric columns for scatter plot
numeric_columns = penguins.select_dtypes(include=['float64', 'int64']).columns
# drop year
numeric_columns = numeric_columns.drop('year')

# scatter plot
st.write("### Scatter Plot")
x_axis = st.selectbox('Select X-axis variable', numeric_columns)
y_axis = st.selectbox('Select Y-axis variable', numeric_columns, index=1)

if x_axis and y_axis:
    fig, ax = plt.subplots()
    sns.scatterplot(data=penguins, x=x_axis, y=y_axis, hue='species', ax=ax)
    st.pyplot(fig)

# display the dataframe as a table
st.write("### Dataset")
st.dataframe(penguins)

# footer
st.write("Data Source: [palmerpenguins](https://github.com/allisonhorst/palmerpenguins)")