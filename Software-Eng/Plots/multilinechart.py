import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Preparing data
# Entering data value for actual_max_temp, actual_min_temp, and actual_mean_temp in line mode.
trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='actual_max_temp')
trace2 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='actual_min_temp')
trace3 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='actual_mean_temp')
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='The actual max, min, and mean temperatures of each month in weather statistics', xaxis_title="date",
                   yaxis_title="Number of actual temperatures")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')
