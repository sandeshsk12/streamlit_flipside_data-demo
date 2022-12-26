# importing necessary packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st 

# import data from flipside 
daily_price_info_of_luna_url = "https://node-api.flipsidecrypto.com/api/v2/queries/5a8cda2b-30f4-4179-a91b-86aace3a0d69/data/latest"
daily_price_info_of_luna_data = pd.read_json(daily_price_info_of_luna_url)

# Create a plot of the DATETIME and LUNA_PRICE columns
plt.plot(daily_price_info_of_luna_data["DATETIME"],daily_price_info_of_luna_data["LUNA_PRICE"])

# Save the plot to a file
plt.savefig("plot.png")

# Display the plot as an image
st.image("plot.png")

c1,c2=st.columns(2)
c1.image("plot.png")
