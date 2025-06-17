import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# -------- Parameters --------
ticker = "AAPL"  # You can change this to any valid ticker
discount_rate = 0.08  # 8% annual discount rate

# -------- Fetch Financials --------
stock = yf.Ticker(ticker)
income_stmt = stock.financials.T  # Transposed: Rows become years

# -------- Extract Revenue and Costs --------
try:
    revenue = income_stmt['Total Revenue'].values
    cogs = income_stmt['Cost Of Revenue'].values
    years = income_stmt.index.year
except KeyError as e:
    print(f"Missing key in financial data: {e}")
    exit()

# -------- Calculate Net Cash Flows --------
cash_flows = revenue - cogs

# -------- Forecast NPV --------
npv = sum(cf / ((1 + discount_rate) ** (i + 1)) for i, cf in enumerate(cash_flows))

# -------- Display Results --------
df = pd.DataFrame({
    'Year': years,
    'Revenue': revenue,
    'COGS': cogs,
    'Net Cash Flow': cash_flows
})
print(df)
print(f"\nNet Present Value (NPV) for {ticker}: ${npv:,.2f}")

# -------- Optional: Plot Cash Flows --------
plt.plot(years, cash_flows, marker='o')
plt.title(f'Net Cash Flows for {ticker}')
plt.xlabel('Year')
plt.ylabel('Cash Flow ($)')
plt.grid(True)
plt.tight_layout()
plt.savefig("npv_cashflows.png")
plt.show()
