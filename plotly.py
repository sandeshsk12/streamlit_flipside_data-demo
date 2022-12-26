# importing necessary packages

import pandas as pd 
import numpy as np 
import plotly.express  as px 
import streamlit as st 

# Allows us to create graph objects for making more customized plots
import plotly.graph_objects as go

# import data from flipside 
daily_price_info_of_luna_url = "https://node-api.flipsidecrypto.com/api/v2/queries/5a8cda2b-30f4-4179-a91b-86aace3a0d69/data/latest"
daily_price_info_of_luna_data = pd.read_json(daily_price_info_of_luna_url)

# Use data to make one plot
fig=px.line(daily_price_info_of_luna_data, x='DATETIME', y='LUNA_PRICE', labels={'x':'Date', 'y':'Price'})

# Display the plot in a web application
st.write("Simple graph")
st.plotly_chart(fig)

# Further style the figure
fig.update_layout(title='Daily price of luna',
                   xaxis_title='Price', yaxis_title='Date')

# Go crazy styling the figure
fig.update_layout(
    # Shows gray line without grid, styling fonts, linewidths and more
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    # Turn off everything on y axis
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    autosize=False,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    showlegend=False,
    plot_bgcolor='white'
)
# Display the plot in a web application
st.write("Styled graph")
st.plotly_chart(fig)

