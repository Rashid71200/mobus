import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import time
from collections import deque
import plotly.graph_objs as go
import random
from dash.exceptions import PreventUpdate


max_length = 50
power_factor = deque(maxlen=max_length)
volt = deque(maxlen=max_length)
current = deque(maxlen=max_length)
hz = deque(maxlen=max_length)


data_dict = {'Blades (Rotation Speed)': volt,
             'Power Produced': current,
             'Energy Losses': hz,
             }



def update_values(power_factor, volt, current, hz):

    power_factor.append(time.time())
    if len(power_factor) == 1:
        #starting values for each category
        volt.append(random.randrange(60, 300))
        current.append(random.randrange(30, 430))
        hz.append(random.randrange(10, 35))
    else:
        for get_data in [volt, current, hz]:
            get_data.append(get_data[-1]+get_data[-1]*random.uniform(-0.0001, 0.0001))

    return power_factor, volt, current, hz

power_factor, volt, current, hz = update_values(power_factor, volt, current, hz)




app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('corona-logo-1.jpg'),
                     id='corona-image',
                     style={
                         "height": "60px",
                         "width": "auto",
                         "margin-bottom": "25px",
                     },
                     )
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H3("Smart Energy Monitoring Dashboard", style={"margin-bottom": "0px", 'color': 'white'}),
                html.H5("By Azaharul Rashid", style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="one-half column", id="title"),

        html.Div([
            html.H6('Last Updated: '  + '  00:01 (UTC)',
                    style={'color': 'orange'}),

        ], className="one-third column", id='title1'),

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    html.Div([
        html.Div([
            html.H6(children='Average Voltage',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{volt}V",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),

            html.P('',
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 15,
                       'margin-top': '-18px'}
                   )], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Current (A)',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{current}A",
                   style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 40}
                   ),

            html.P('',
                   style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 15,
                       'margin-top': '-18px'}
                   )], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Power factor (PF)',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{power_factor}%",
                   style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 40}
                   ),

            html.P('',
                   style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 15,
                       'margin-top': '-18px'}
                   )], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Frequency(Hz)',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{hz}",
                   style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 40}
                   ),

            html.P('new:  ',
                   style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 15,
                       'margin-top': '-18px'}
                   )], className="card_container three columns")

    ], className="row flex-display"),

    html.Div([
        html.Div([

        ], className="create_container three columns", id="cross-filter-options"),
            html.Div([
                  
                              ], className="create_container four columns"),

                    html.Div([
          
                    ], className="create_container five columns"),

        ], className="row flex-display"),


    ], id="mainContainer",
    style={"display": "flex", "flex-direction": "column"})


# Create pie chart (total casualties)



# Create bar chart (show new cases)


# Create scattermapbox chart





if __name__ == '__main__':
    app.run_server(debug=True)
