import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd
from sklearn import datasets
# worker: python app.py
#Create Data
housing_dict = datasets.fetch_california_housing()
data = pd.DataFrame(housing_dict['data'])
data.columns = housing_dict['feature_names']

#Create a plotly graph to be used by dcc.Graph()
fig = px.scatter(data,x='AveRooms',y='AveBedrms',title='Relation b/w Rooms & Bedrooms')
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