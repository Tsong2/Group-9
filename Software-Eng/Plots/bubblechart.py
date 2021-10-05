import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by NOC Column
new_df = df.groupby(['month']).agg(
    {'average_min_temp': 'sum', 'average_max_temp': 'sum'}
).reset_index()

#'record_min_temp_year': 'sum', 'record_max_temp_year': 'sum',
# Preparing data
data = [go.Scatter(x=new_df['average_min_temp'],
                   y=new_df['average_max_temp'],
                   text=new_df['month'],
                   mode='markers',
                   marker=dict(size=new_df['average_max_temp'] / 100, color=new_df['average_max_temp'] / 100, showscale=True))
        ]

# Preparing layout
layout = go.Layout(title='The average min and max temperatures of each month in weather statistics', xaxis_title="month",
                   yaxis_title="Number of average min and max temperatures", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')
