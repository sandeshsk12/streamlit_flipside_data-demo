# importing necessary packages
import pandas as pd 
import numpy as np 
import altair as alt
import streamlit as st 

# import data from flipside 
daily_price_info_of_luna_url = "https://node-api.flipsidecrypto.com/api/v2/queries/5a8cda2b-30f4-4179-a91b-86aace3a0d69/data/latest"
daily_price_info_of_luna_data = pd.read_json(daily_price_info_of_luna_url)

# Create an Altair chart with a line plot of the DATETIME and LUNA_PRICE columns
fig = alt.Chart(daily_price_info_of_luna_data).mark_line().encode(
    x='DATETIME',
    y='LUNA_PRICE'
)

# Display the chart in a Streamlit app
st.altair_chart(fig)
