import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit app title
st.title('Stock Analysis Dashboard')

# User input for stock ticker
ticker = st.text_input('Enter Stock Ticker (e.g., AAPL)', 'AAPL').upper()

# Fetch data
data = yf.download(ticker, period="1d", interval="1m")

# Estimate Buyer and Seller Volume
data['Price Change'] = data['Close'].diff()
data['Buy Volume'] = data['Volume'].where(data['Price Change'] > 0, 0)
data['Sell Volume'] = data['Volume'].where(data['Price Change'] < 0, 0)

# Calculate accumulated Buy and Sell Volume
data['Accumulated Buy Volume'] = data['Buy Volume'].cumsum()
data['Accumulated Sell Volume'] = data['Sell Volume'].cumsum()


# Display stock price
st.subheader('Stock Price Over Time')
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(data.index, data['Close'], label='Close Price', color='blue')
ax.set_title('Stock Price Over Time')
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.legend()
ax.grid()
st.pyplot(fig)

# Display accumulated volumes
st.subheader('Accumulated Buy and Sell Volumes Over Time')
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(data.index, data['Accumulated Buy Volume'], label='Accumulated Buy Volume', color='green')
ax.plot(data.index, data['Accumulated Sell Volume'], label='Accumulated Sell Volume', color='red')
ax.set_title('Accumulated Buy and Sell Volumes Over Time')
ax.set_xlabel('Time')
ax.set_ylabel('Accumulated Volume')
ax.legend()
ax.grid()
st.pyplot(fig)
