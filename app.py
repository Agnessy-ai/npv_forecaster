import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="NPV Forecaster", layout="centered")

# --- Title ---
st.title("📊 Project Valuation (NPV) Dashboard")
st.markdown("Forecast Net Present Value (NPV) based on real-time financials")

# --- User Inputs ---
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT)", value="AAPL")
discount_rate = st.slider("Discount Rate (%)", 0.0, 20.0, 8.0) / 100

if st.button("Run Forecast"):
    try:
        stock = yf.Ticker(ticker)
        income_stmt = stock.financials.T  # Transpose so rows = years

        # Validate required fields
        if 'Total Revenue' not in income_stmt.columns or 'Cost Of Revenue' not in income_stmt.columns:
            st.warning("This ticker does not contain required financial data.")
            st.stop()

        # Extract and clean data
        revenue = pd.to_numeric(income_stmt['Total Revenue'], errors='coerce')
        cogs = pd.to_numeric(income_stmt['Cost Of Revenue'], errors='coerce')
        years = [str(idx.year) for idx in income_stmt.index]

        # Drop any rows with missing values
        valid_idx = ~(revenue.isna() | cogs.isna())
        revenue = revenue[valid_idx]
        cogs = cogs[valid_idx]
        years = [y for i, y in enumerate(years) if valid_idx.iloc[i]]
        cash_flows = revenue.values - cogs.values

        # Calculate NPV
        npv = sum(cf / ((1 + discount_rate) ** (i + 1)) for i, cf in enumerate(cash_flows))

        # --- Display Table ---
        df = pd.DataFrame({
            'Year': years,
            'Revenue ($)': revenue.values,
            'COGS ($)': cogs.values,
            'Net Cash Flow ($)': cash_flows
        })
        st.subheader(f"📘 Financial Data for {ticker.upper()}")
        st.dataframe(df.style.format({
            'Revenue ($)': "{:,.2f}",
            'COGS ($)': "{:,.2f}",
            'Net Cash Flow ($)': "{:,.2f}"
        }))

        # --- Display NPV ---
        st.metric(label="📈 Net Present Value (NPV)", value=f"${float(npv):,.2f}")

        # --- Plot ---
        st.subheader("📉 Net Cash Flows Over Time")
        fig, ax = plt.subplots()
        ax.plot(years, cash_flows, marker='o', linestyle='-', color='green')
        ax.set_xlabel("Year")
        ax.set_ylabel("Cash Flow ($)")
        ax.set_title(f"Net Cash Flows for {ticker.upper()}")
        ax.grid(True)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
