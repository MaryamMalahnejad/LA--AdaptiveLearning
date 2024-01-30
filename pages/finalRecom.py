import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_html_components as html
import urllib.parse
from sqlalchemy import create_engine,text


#loading Data from DB
params = urllib.parse.quote_plus(r'Driver={ODBC Driver 18 for SQL Server};Server=tcp:adaptive-learning-server.database.windows.net,1433;Database=adaptive_learning_db;Uid=superadmin;Pwd=Poorpassword@2024;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str,echo=True)

connection = engine_azure.connect()
print("Connection successful !!!!")

app = dash.Dash(__name__)


database_data = "Based on your responses, our recommendation for you is Visaul Materials(like: Quzzes and Interactive Apps or Interactive Videos) "

layout = html.Div([
    html.H2("Here is your recommendation:", style={'textAlign': 'center', 'fontSize': '1.5em'}),
    html.H3("Based on your responses, our recommendation for you is:", style={'textAlign': 'center'}),
    html.H4("Visaul Materials(like: Quzzes and Interactive Apps or Interactive Videos)", style={'textAlign': 'center', 'color':'red'}),
    html.Div(" ", style={'marginTop': '20px'}),
   # dcc.Textarea(id='feedback-input', value=database_data, style={'width': '100%', 'height': '100px'}),
    html.Div(style={'textAlign': 'center'}, children=[
        html.Div("Give us a thumbs up if you find it helpful or not?", style={'marginTop': '20px'}),
        html.Div([
            html.Button(id='thumbs-up-button', children='👍', n_clicks=0),
            html.Button(id='thumbs-down-button', children='👎', n_clicks=0),
        ], style={'display': 'flex', 'justifyContent': 'center', 'marginTop': '10px'}),
    ]),
    html.Div(id='button-output', style={'textAlign': 'center', 'marginTop': '20px'}),
    html.Img(src='..\\assets\\animation.gif', alt="Project Photo", style={'width': '50%', 'margin': 'auto', 'display': 'block'})

])

# callback for thumbs-up button
@app.callback(
    Output('button-output', 'children'),
    [Input('thumbs-up-button', 'n_clicks')]
)
def update_output_thumbs_up(n_clicks):
    if n_clicks > 0:
        return "Thank you for your feedback!"

# callback for thumbs-down button
@app.callback(
    Output('button-output', 'children'),
    [Input('thumbs-down-button', 'n_clicks')]
)
def update_output_thumbs_down(n_clicks):
    if n_clicks > 0:
        return "Thank you for your feedback!"


if __name__ == '__main__':
    app.run_server(debug=True)
