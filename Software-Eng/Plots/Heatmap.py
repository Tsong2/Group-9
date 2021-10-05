import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')


# Preparing data
# Entering the day for x-axis, month for y-axis, entering z-axis for data on record_max_temp_year
# color scale on Jet color
data = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['record_max_temp_year'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='The record of max temperature on day of week and month of year', xaxis_title="Day of week",
                   yaxis_title="Month of year")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Heatmap.html')
