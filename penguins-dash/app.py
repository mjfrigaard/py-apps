import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Load the dataset
url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
df = pd.read_csv(url)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Palmer Penguins Data Dashboard")
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='x-axis',
                options=[{'label': col, 'value': col} for col in df.select_dtypes(include=['float64', 'int64']).columns],
                value='bill_length_mm',
                clearable=False
            )
        ], width=6),
        dbc.Col([
            dcc.Dropdown(
                id='y-axis',
                options=[{'label': col, 'value': col} for col in df.select_dtypes(include=['float64', 'int64']).columns],
                value='bill_depth_mm',
                clearable=False
            )
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='scatter-plot')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
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
        ], width=12)
    ])
])

# Callback to update the scatter plot
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-axis', 'value'),
     Input('y-axis', 'value')]
)
def update_scatter_plot(x_axis, y_axis):
    fig = px.scatter(
        df, x=x_axis, y=y_axis, color='species',
        labels={x_axis: x_axis, y_axis: y_axis},
        title=f'Scatter Plot of {x_axis} vs {y_axis}'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
