import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Preparing data
data = [go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='actual_max_temp')]

# Preparing layout
layout = go.Layout(title='The actual max temperature of each month in weather statistics', xaxis_title="date",
                   yaxis_title="Number of actual temperatures")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')
