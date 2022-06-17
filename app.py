import dash
from random import randint
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

#Create Data
x = [randint(1,1000) for i in range(10000)]
y = [randint(1,1000) for i in range(10000)]
data = pd.DataFrame([x,y]).T
data.columns = ['x','y']

#Create a plotly graph to be used by dcc.Graph()
fig = px.scatter(data,x='x',y='y',title='Relation b/w Rooms & Bedrooms')
app = dash.Dash(__name__)
app.title = "House Data Analysis"
server = app.server

app.layout = html.Div(
         id="app-container"
        ,children=[
             html.H1("Relation b/w Rooms & Bedrooms")
            ,html.P("Results in USD/oz")
            ,dcc.Graph(figure=fig)
        ]
    )

if __name__ == "__main__":
    app.run_server(debug=True)