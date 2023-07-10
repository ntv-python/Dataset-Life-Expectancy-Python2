import dash
import dash_bootstrap_components as dbc
from dash import dash_table
import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from dash_bootstrap_templates import load_figure_template
import numpy as np
import os




my_data = pd.read_csv('Life Expectancy Data.csv') 



countries = my_data['Country'].unique()
years = my_data['Year'].unique()


custom_colors = ['#331177', '#F9C70C']  # Custom colors: Indigo and Amber
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH])


# Data for Pie chart
gdp_sum_by_status_year = my_data.groupby(['Year', 'Status'])['GDP'].sum().reset_index()


initial_year = years[0]
gdp_sum_by_status_initial = gdp_sum_by_status_year[gdp_sum_by_status_year['Year'] == initial_year]
pie_data = go.Pie(
    labels=gdp_sum_by_status_initial['Status'],
    values=gdp_sum_by_status_initial['GDP'],
    hole=0.3,
    marker=dict(colors=custom_colors),
)


app.layout = dbc.Container(
    [
        html.Div(
            [
                html.P("😄", className="header-emoji text-center", style={'font-size': '48px', 'color': 'black'}),
                html.H1(
                    "Life Expectancy Dataset",
                    className="header-title",
                    style={
                        'color': 'black',  # Change the color to black
                        'margin': '4px auto',
                        'text-align': 'center',
                        'max-width': '384px',
                        'font-size': '40px',
                        'font-family': 'Yeseva One',
                        'letter-spacing': '2px'
                    },
                ),
            ],
            className="header-banner",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Distribution of GDP by Status", className="subtitle",
                                               style={'color': 'black', 'text-align': 'center'}),  # Change the color to black and align center
                                dbc.CardBody(
                                    [
                                        dcc.Dropdown(
                                            id='year-dropdown-pie',
                                            options=[{'label': year, 'value': year} for year in years],
                                            value=initial_year,
                                            clearable=False,
                                            className='dropdown'
                                        ),
                                        dcc.Graph(
                                            id='pie-chart',
                                            figure={'data': [pie_data]},
                                            style={'height': '400px', 'font-family': 'Yeseva One',
                                                   'color': 'black'}
                                        ),
                                    ],
                                    className="grid-item",
                                ),
                            ],
                            className="card-style",
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader("Life expectancy", className="subtitle",
                                               style={'color': 'black', 'text-align': 'center'}),  # Change the color to black and align center
                                dbc.CardBody(
                                    [
                                        dcc.Dropdown(
                                            id='country-dropdown',
                                            options=[{'label': country, 'value': country} for country in countries],
                                            value=countries[0],
                                            className='dropdown'
                                        ),
                                        dcc.Graph(
                                            id='line-chart',
                                            style={'height': '400px', 'background-color': 'rgba(0,0,0,0)',
                                                   'color': 'black', 'font-family': 'Yeseva One'}  # Change the color to black
                                        ),
                                    ],
                                    className="grid-item",
                                ),
                            ],
                            className="card-style",
                        ),
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Adult Mortality", className="subtitle",
                                               style={'color': 'black', 'text-align': 'center'}),  # Change the color to black and align center
                                dbc.CardBody(
                                    [
                                        dcc.Graph(
                                            id='histogram',
                                            style={'height': '400px', 'width': '550px', 'font-family': 'Yeseva One',
                                                   'color': 'black'}  # Change the color to black
                                        ),
                                        dcc.Slider(
                                            id='std-slider',
                                            min=0,
                                            max=5,
                                            step=0.1,
                                            value=1,
                                            marks={i: f"{i}" for i in range(6)}
                                        )
                                    ],
                                    className="grid-item",
                                ),
                            ],
                            className="card-style",
                        ),
                        dbc.Card(
                            [
                                dbc.CardHeader("BMI Distribution", className="subtitle",
                                               style={'color': 'black', 'text-align': 'center'}),
                                dbc.CardBody(
                                    [
                                        dcc.Dropdown(
                                            id='year-dropdown-table',
                                            options=[{'label': year, 'value': year} for year in years],
                                            value=None,
                                            placeholder='Select a year',
                                            clearable=True,
                                            className='dropdown'
                                        ),
                                        dash_table.DataTable(
                                            id='data-table',
                                            columns=[{'name': 'Country', 'id': 'Country'}, {'name': 'BMI', 'id': 'bmi'}],
                                            data=[],
                                            style_cell={'textAlign': 'center', 'font-family': 'Times New Roman',
                                                        'color': '#000000'},
                                            style_header={
                                                'backgroundColor': 'rgb(230, 230, 230)',
                                                'fontWeight': 'bold',
                                                'text-align': 'center'  # Align table header text to center
                                            },
                                            page_size=10,
                                            sort_action='native',
                                            filter_action='native'
                                        ),
                                    ],
                                    className="grid-item",
                                ),
                            ],
                            className="card-style",
                        ),
                    ],
                    md=6,  
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Total expenditure", className="subtitle",
                                               style={'color': 'black', 'text-align': 'center'}),  # Change the color to black and align center
                                dbc.CardBody(
                                    [
                                        dcc.Dropdown(
                                            id='country-dropdown-expenditure',
                                            options=[{'label': country, 'value': country} for country in countries],
                                            value=countries[0],
                                            className='dropdown'
                                        ),
                                        dcc.Graph(
                                            id='scatter-line-bar-chart',
                                            style={'height': '400px', 'background-color': 'rgba(0,0,0,0)',
                                                   'color': 'black', 'font-family': 'Yeseva One'}  # Change the color to black
                                        ),
                                    ],
                                    className="grid-item",
                                ),
                            ],
                            className="card-style",
                        ),
                    ],
                    md=12,
                ),
            ],
            className="grid-container",
            style={'margin': '100px'},  # Increase the spacing between the upper and lower graphs
        ),
    ],
    className="container",
)




@app.callback(
    Output('pie-chart', 'figure'),
    [Input('year-dropdown-pie', 'value')]
)
def update_pie_chart(selected_year):
    gdp_sum_by_status_selected = gdp_sum_by_status_year[gdp_sum_by_status_year['Year'] == selected_year]
    updated_pie_data = go.Pie(
        labels=gdp_sum_by_status_selected['Status'],
        values=gdp_sum_by_status_selected['GDP'],
        hole=0.3,
        marker=dict(colors=custom_colors),
    )
    return {'data': [updated_pie_data]}




@app.callback(
    Output('line-chart', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_line_chart(selected_country):
    # Filter the data on the selected country
    country_data = my_data[my_data['Country'] == selected_country]


    line_data = go.Scatter(
        x=country_data['Year'],
        y=country_data['Life expectancy'],
        mode='lines+markers',
        marker=dict(color='#331177', size=6),
        line=dict(width=2)
    )
    return {'data': [line_data]}




@app.callback(
    Output('scatter-line-bar-chart', 'figure'),
    [Input('country-dropdown-expenditure', 'value')]
)
def update_scatter_line_bar_chart(selected_country):
    # Filter the data on the selected country
    country_data = my_data[my_data['Country'] == selected_country]


    scatter_data = go.Scatter(
        x=country_data['Year'],
        y=country_data['Total expenditure'],
        mode='markers',
        marker=dict(color='#331177', size=10)
    )
    line_data = go.Scatter(
        x=country_data['Year'],
        y=country_data['Total expenditure'],
        mode='lines',
        marker=dict(color='#378805'),
        line=dict(width=2)
    )
    bar_data = go.Bar(
        x=country_data['Year'],
        y=country_data['Total expenditure'],
        marker=dict(color='#F9C70C')
    )


    return {'data': [scatter_data, line_data, bar_data]}




@app.callback(
    Output('histogram', 'figure'),
    [Input('std-slider', 'value')]
)
def update_histogram(std):
    histogram_data = go.Histogram(
        x=my_data['Adult Mortality'],
        marker=dict(color=custom_colors[0]),
        nbinsx=50,
        histnorm='probability density',
        autobinx=False,
        xbins=dict(start=np.min(my_data['Adult Mortality']), end=np.max(my_data['Adult Mortality']), size=std)
    )
    layout = {
        'title': 'Adult Mortality Histogram',
        'xaxis': {'title': 'Adult Mortality'},
        'yaxis': {'title': 'Probability Density'},
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'plot_bgcolor': 'rgba(0,0,0,0)',
    }
    return {'data': [histogram_data], 'layout': layout}




@app.callback(
    Output('data-table', 'data'),
    [Input('year-dropdown-table', 'value')]
)
def update_table(selected_year):
    if selected_year:
        filtered_data = my_data[my_data['Year'] == selected_year]
        sorted_data = filtered_data.sort_values(by='bmi', ascending=True)
        return sorted_data[['Country', 'bmi']].to_dict('records')
    else:
        return []




if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)


