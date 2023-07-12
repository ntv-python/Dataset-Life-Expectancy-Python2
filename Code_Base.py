
import dash
import dash_bootstrap_components as dbc
from dash import dash_table
import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import numpy as np
import os

my_data = pd.read_csv('Life Expectancy Data.csv') 



country_to_continent = {
    'Afghanistan': 'Asia',
    'Albania': 'Europe',
    'Algeria': 'Africa',
    'Andorra': 'Europe',
    'Angola': 'Africa',
    'Antigua and Barbuda': 'North America',
    'Argentina': 'South America',
    'Armenia': 'Asia',
    'Australia': 'Oceania',
    'Austria': 'Europe',
    'Azerbaijan': 'Asia',
    'Bahamas': 'North America',
    'Bahrain': 'Asia',
    'Bangladesh': 'Asia',
    'Barbados': 'North America',
    'Belarus': 'Europe',
    'Belgium': 'Europe',
    'Belize': 'North America',
    'Benin': 'Africa',
    'Bhutan': 'Asia',
    'Bolivia': 'South America',
    'Bosnia and Herzegovina': 'Europe',
    'Botswana': 'Africa',
    'Brazil': 'South America',
    'Brunei': 'Asia',
    'Bulgaria': 'Europe',
    'Burkina Faso': 'Africa',
    'Burundi': 'Africa',
    'Cambodia': 'Asia',
    'Cameroon': 'Africa',
    'Canada': 'North America',
    'Cape Verde': 'Africa',
    'Central African Republic': 'Africa',
    'Chad': 'Africa',
    'Chile': 'South America',
    'China': 'Asia',
    'Colombia': 'South America',
    'Comoros': 'Africa',
    'Congo (Brazzaville)': 'Africa',
    'Congo (Kinshasa)': 'Africa',
    'Costa Rica': 'North America',
    'Croatia': 'Europe',
    'Cuba': 'North America',
    'Cyprus': 'Asia',
    'Czech Republic': 'Europe',
    'Denmark': 'Europe',
    'Djibouti': 'Africa',
    'Dominica': 'North America',
    'Dominican Republic': 'North America',
    'East Timor': 'Asia',
    'Ecuador': 'South America',
    'Egypt': 'Africa',
    'El Salvador': 'North America',
    'Equatorial Guinea': 'Africa',
    'Eritrea': 'Africa',
    'Estonia': 'Europe',
    'Ethiopia': 'Africa',
    'Fiji': 'Oceania',
    'Finland': 'Europe',
    'France': 'Europe',
    'Gabon': 'Africa',
    'Gambia': 'Africa',
    'Georgia': 'Asia',
    'Germany': 'Europe',
    'Ghana': 'Africa',
    'Greece': 'Europe',
    'Grenada': 'North America',
    'Guatemala': 'North America',
    'Guinea': 'Africa',
    'Guinea-Bissau': 'Africa',
    'Guyana': 'South America',
    'Haiti': 'North America',
    'Honduras': 'North America',
    'Hungary': 'Europe',
    'Iceland': 'Europe',
    'India': 'Asia',
    'Indonesia': 'Asia',
    'Iran': 'Asia',
    'Iraq': 'Asia',
    'Ireland': 'Europe',
    'Israel': 'Asia',
    'Italy': 'Europe',
    'Ivory Coast': 'Africa',
    'Jamaica': 'North America',
    'Japan': 'Asia',
    'Jordan': 'Asia',
    'Kazakhstan': 'Asia',
    'Kenya': 'Africa',
    'Kiribati': 'Oceania',
    'Korea, North': 'Asia',
    'Korea, South': 'Asia',
    'Kuwait': 'Asia',
    'Kyrgyzstan': 'Asia',
    'Laos': 'Asia',
    'Latvia': 'Europe',
    'Lebanon': 'Asia',
    'Lesotho': 'Africa',
    'Liberia': 'Africa',
    'Libya': 'Africa',
    'Liechtenstein': 'Europe',
    'Lithuania': 'Europe',
    'Luxembourg': 'Europe',
    'Macedonia': 'Europe',
    'Madagascar': 'Africa',
    'Malawi': 'Africa',
    'Malaysia': 'Asia',
    'Maldives': 'Asia',
    'Mali': 'Africa',
    'Malta': 'Europe',
    'Marshall Islands': 'Oceania',
    'Mauritania': 'Africa',
    'Mauritius': 'Africa',
    'Mexico': 'North America',
    'Micronesia': 'Oceania',
    'Moldova': 'Europe',
    'Monaco': 'Europe',
    'Mongolia': 'Asia',
    'Montenegro': 'Europe',
    'Morocco': 'Africa',
    'Mozambique': 'Africa',
    'Myanmar': 'Asia',
    'Namibia': 'Africa',
    'Nauru': 'Oceania',
    'Nepal': 'Asia',
    'Netherlands': 'Europe',
    'New Zealand': 'Oceania',
    'Nicaragua': 'North America',
    'Niger': 'Africa',
    'Nigeria': 'Africa',
    'Norway': 'Europe',
    'Oman': 'Asia',
    'Pakistan': 'Asia',
    'Palau': 'Oceania',
    'Panama': 'North America',
    'Papua New Guinea': 'Oceania',
    'Paraguay': 'South America',
    'Peru': 'South America',
    'Philippines': 'Asia',
    'Poland': 'Europe',
    'Portugal': 'Europe',
    'Qatar': 'Asia',
    'Romania': 'Europe',
    'Russia': 'Asia',
    'Rwanda': 'Africa',
    'Saint Kitts and Nevis': 'North America',
    'Saint Lucia': 'North America',
    'Saint Vincent and the Grenadines': 'North America',
    'Samoa': 'Oceania',
    'San Marino': 'Europe',
    'Sao Tome and Principe': 'Africa',
    'Saudi Arabia': 'Asia',
    'Senegal': 'Africa',
    'Serbia': 'Europe',
    'Seychelles': 'Africa',
    'Sierra Leone': 'Africa',
    'Singapore': 'Asia',
    'Slovakia': 'Europe',
    'Slovenia': 'Europe',
    'Solomon Islands': 'Oceania',
    'Somalia': 'Africa',
    'South Africa': 'Africa',
    'South Sudan': 'Africa',
    'Spain': 'Europe',
    'Sri Lanka': 'Asia',
    'Sudan': 'Africa',
    'Suriname': 'South America',
    'Swaziland': 'Africa',
    'Sweden': 'Europe',
    'Switzerland': 'Europe',
    'Syria': 'Asia',
    'Taiwan': 'Asia',
    'Tajikistan': 'Asia',
    'Tanzania': 'Africa',
    'Thailand': 'Asia',
    'Togo': 'Africa',
    'Tonga': 'Oceania',
    'Trinidad and Tobago': 'North America',
    'Tunisia': 'Africa',
    'Turkey': 'Asia',
    'Turkmenistan': 'Asia',
    'Tuvalu': 'Oceania',
    'Uganda': 'Africa',
    'Ukraine': 'Europe',
    'United Arab Emirates': 'Asia',
    'United Kingdom': 'Europe',
    'United States': 'North America',
    'Uruguay': 'South America',
    'Uzbekistan': 'Asia',
    'Vanuatu': 'Oceania',
    'Vatican City': 'Europe',
    'Venezuela': 'South America',
    'Vietnam': 'Asia',
    'Yemen': 'Asia',
    'Zambia': 'Africa',
    'Zimbabwe': 'Africa'
}


my_data['Total Expenditure'] = my_data['Totalexpenditure']


countries = my_data['Country'].unique()
years = my_data['Year'].unique()


continents = list(set(country_to_continent.values()))




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server

# Data for Pie chart
gdp_sum_by_status_year = my_data.groupby(['Year', 'Status'])['GDP'].sum().reset_index()


initial_year = years[0]
initial_continent = continents[0]
gdp_sum_by_status_initial = gdp_sum_by_status_year[gdp_sum_by_status_year['Year'] == initial_year]
pie_data = go.Pie(
    labels=gdp_sum_by_status_initial['Status'],
    values=gdp_sum_by_status_initial['GDP'],
    hole=0.3,
)


app.layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Div(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H1(
                            "Life Expectancy Dataset",
                            className="header-title-big text-center",
                        ),
                        html.Br(),
                        html.P(
                            "Welcome to the interactive dashboard showcasing life expectancy data. "
                            "You can explore various aspects of the dataset, including the distribution "
                            "of GDP by status, globally BMI distribution, adult mortality over time, total expenditure, and a "
                            "life expectancy map.",
                            className="header-description text-center",
                        ),
                    ],
                    className="header",
                ),
                html.Br(),
               
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Distribution of GDP by Status",
                                    className="card-header text-center font-weight-bold",  # Added font-weight-bold class
                                    style={"background-color": "transparent", "font-size": "20px"},  # Added font-size style
                                ),
                                dbc.CardBody(
                                    [
                                        html.P("Choose a year", className="card-subtitle text-center"),  # Added text-center class
                                        dcc.Dropdown(
                                            id='year-dropdown',
                                            options=[{'label': year, 'value': year} for year in years],
                                            value=initial_year,
                                            clearable=False,
                                            className='dropdown'
                                        ),
                                        dcc.Graph(
                                            id='pie-chart',
                                            style={'height': '400px'}
                                        ),
                                        dash_table.DataTable(
                                            id='data-table',
                                            columns=[{'name': 'Country', 'id': 'Country'},
                                                     {'name': 'BMI', 'id': 'BMI'}],
                                            data=[],
                                            style_cell={'textAlign': 'center'},
                                            style_header={
                                                'backgroundColor': 'rgb(230, 230, 230)',
                                                'fontWeight': 'bold',
                                                'textAlign': 'center'
                                            },
                                            page_size=10,
                                            sort_action='native',
                                            filter_action='native'
                                        ),
                                    ],
                                    className="card-content",
                                    style={"border": "none"}
                                ),
                            ],
                            style={"border": "none", "box-shadow": "none"},
                        ),
                        html.Br(),
                        html.Br(),
                    ],
                    md=6,
                    className="align-self-center",
                ),


                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Adult Mortality and Total Expenditure",
                                    className="card-header text-center font-weight-bold",  # Added font-weight-bold class
                                    style={"background-color": "transparent", "font-size": "20px"},  # Added font-size style
                                ),
                                dbc.CardBody(
                                    [
                                        html.P("Choose a country", className="card-subtitle text-center"),  # Added text-center class
                                        dcc.Dropdown(
                                            id='country-dropdown',
                                            options=[{'label': country, 'value': country} for country in countries],
                                            value=countries[0],
                                            className='dropdown'
                                        ),
                                        dcc.Graph(
                                            id='line-chart',
                                            style={'height': '400px','width':'600px'}
                                        ),
                                        dcc.Graph(
                                            id='scatter-line-bar-chart',
                                            style={'height': '450px', 'width':'570px'}
                                        ),
                                    ],
                                    className="card-content",
                                    style={"border": "none"}
                                ),
                            ],
                            style={"border": "none", "box-shadow": "none"},
                        ),
                    ],
                    md=6,
                    className="align-self-center",
                ),
               
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Life Expectancy Map",
                                    className="card-header text-center font-weight-bold",  # Added font-weight-bold class
                                    style={"background-color": "transparent", "font-size": "20px"},  # Added font-size style
                                ),
                                html.Br(),
                                dbc.CardBody(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Checklist(
                                                        id='continent-checkboxes',
                                                        options=[{'label': continent, 'value': continent} for
                                                                 continent in continents],
                                                        value=[initial_continent],
                                                    
                                                    ),
                                                    md=1
                                                ),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        id='continent-country-dropdown',
                                                        options=[],
                                                        value='',
                                                        className='dropdown',
                                                        clearable=False
                                                    ),
                                                    md=4
                                                ),
   
 
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        id='life-year-dropdown',
                                                        options=[{'label': year, 'value': year} for year in years],
                                                        value=initial_year,
                                                        clearable=False,
                                                        className='dropdown'
                                                    ),
                                                    md=4
                                                ),
                                            ],
                                            className='align-items-start justify-content-center',
                                        ),
                                        html.Br(),


                                        dcc.Graph(
                                            id='life-expectancy-map',
                                            style={'height': '500px'}
                                        ),
                                    ],
                                    className="card-content",
                                    style={"border": "none"}
                                ),
                            ],
                            className="card",
                            style={"border": "none", "box-shadow": "none"},
                        ),
                    ],
                    md=12,
                    className="align-self-center",
                ),
            ],
            className="content justify-content-center",
        ),
    ],
    className="container d-flex flex-column justify-content-center align-items-center",
    fluid=True,
)




@app.callback(
    Output('pie-chart', 'figure'),
    Output('data-table', 'data'),
    [Input('year-dropdown', 'value')]
)
def update_pie_chart_and_table(selected_year):
    gdp_sum_by_status_selected = gdp_sum_by_status_year[gdp_sum_by_status_year['Year'] == selected_year]
    updated_pie_data = go.Pie(
        labels=gdp_sum_by_status_selected['Status'],
        values=gdp_sum_by_status_selected['GDP'],
        hole=0.3,
        marker_colors=["#efe350ff", "#6b4596ff"]
    )


    filtered_data = my_data[my_data['Year'] == selected_year]
    sorted_data = filtered_data.sort_values(by='BMI', ascending=True)
    table_data = sorted_data[['Country', 'BMI']].to_dict('records')


    return {'data': [updated_pie_data]}, table_data




@app.callback(
    Output('line-chart', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_line_chart(selected_country):
    country_data = my_data[my_data['Country'] == selected_country]


    line_data = go.Scatter(
        x=country_data['Year'],
        y=country_data['Adult'],
        mode='lines+markers',
        marker=dict(size=6, color='#b8627d'),
        line=dict(width=2, color='#b8627d')
    )
    return {'data': [line_data]}




@app.callback(
    Output('scatter-line-bar-chart', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_scatter_line_bar_chart(selected_country):
    country_data = my_data[my_data['Country'] == selected_country]


    scatter_data = go.Scatter(
        x=country_data['Year'],
        y=country_data['Totalexpenditure'],
        mode='markers',
        marker=dict(size=10)
    )
    line_data = go.Scatter(
        x=country_data['Year'],
        y=country_data['Totalexpenditure'],
        mode='lines',
        line=dict(width=2)
    )
    bar_data = go.Bar(
        x=country_data['Year'],
        y=country_data['Totalexpenditure'],
        marker=dict(
            color=np.linspace(0, 1, len(country_data['Year'])),
            colorscale='Magma',
        )
    )


    return {'data': [scatter_data, line_data, bar_data]}




@app.callback(
    Output('continent-country-dropdown', 'options'),
    Output('continent-country-dropdown', 'value'),
    [Input('continent-checkboxes', 'value')]
)
def update_continent_country_dropdown(selected_continents):
    continent_data = my_data[my_data['Country'].map(country_to_continent).isin(selected_continents)]
    country_options = [{'label': country, 'value': country} for country in continent_data['Country'].unique()]
    return country_options, country_options[0]['value']


@app.callback(
    Output('life-expectancy-map', 'figure'),
    [Input('life-year-dropdown', 'value'),
     Input('continent-country-dropdown', 'value')]
)
def update_life_expectancy_map(selected_year, selected_country):
    year_data = my_data[my_data['Year'] == selected_year]
    country_data = year_data[year_data['Country'] == selected_country]


    fig = px.choropleth(
        data_frame=country_data,
        locations='Country',
        locationmode='country names',
        color='Life',
        hover_name='Country',
        color_continuous_scale='Magma'
    )


    fig.update_layout(
        margin=dict(l=1, r=0, t=30, b=0),
        coloraxis_colorbar=dict(
            title='Life Expectancy',
            x=1.05
        )
    )


    return fig






if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)
    
