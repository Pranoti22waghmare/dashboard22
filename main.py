import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

st.sidebar.title("Option")
option = st.sidebar.selectbox('Which Dashboard',("Charts", "Patterns"))
st.header(option)

if option == "Charts":
  st.subheader("Charts Dashboard")
  symbol =st.sidebar.text_input("Symbol", value="TSLA", max_chars=5)
  st.image(f"https://finviz.com/chart.ashx?t={symbol}&p=w&tas=0")
  st.header(symbol)
  tickerdata = yf.Ticker(symbol)
  tickerdf = tickerdata.history(period="max")
  st.line_chart(tickerdf.Close)
  st.line_chart(tickerdf.Volume)

  # financials
  hodl = tickerdata.institutional_holders
  recom= tickerdata.recommendations
  finan =tickerdata.financials
  balance = tickerdata.balance_sheet
  maj = tickerdata.major_holders
  st.header(hodl)
  st.header(maj)
  st.text(recom)
  st.text(balance)
  st.header(finan)







if option == "Patterns":
  st.subheader("Patterns dashboard")
