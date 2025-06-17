
## 📊 NPV Forecaster
NPV Forecaster is a real-time Streamlit dashboard that calculates the Net Present Value (NPV) of a company based on publicly available financial data. Users input a stock ticker and desired discount rate, and the app automatically pulls revenue and cost data from Yahoo Finance using the yfinance API.

## 🔍 Features
📈 Real-time financial data from Yahoo Finance

🧮 NPV calculation using customizable discount rates

🧾 Interactive financial table showing Revenue, COGS, and Net Cash Flow

📉 Line chart visualization of cash flows over time

💡 Easy-to-use interface built with Streamlit

## 🚀 How It Works
User inputs a stock ticker symbol (e.g., AAPL, TSLA, MSFT)

User selects a discount rate (0–20%)

The app:

Pulls financials (revenue & cost of goods sold)
 
​
 
Results are presented in a table, metric, and a time-series chart

## 📦 Dependencies
streamlit

yfinance

pandas

matplotlib

## Install with:

pip install streamlit yfinance pandas matplotlib

## 🖥️ Running the App

streamlit run app.py
📌 Example Use Case
A finance student or analyst uses the app to evaluate the investment potential of a tech stock under different discount rates, using the company’s reported financials from the past few years.
