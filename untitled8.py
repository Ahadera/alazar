import os
import numpy as np
import pandas as pd
import subprocess
import sys
import yfinance as yf
import streamlit as st
import plotly.graph_objs as go

try:
    import yfinance as yf
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])
    import yfinance as yf

class StockAnalyzer:
    def __init__(self, stocks, start_date, end_date):
        self.stocks = stocks
        self.start_date = start_date
        self.end_date = end_date
        self.data_dict = {}

    def fetch_data(self):
        for stock in self.stocks:
            try:
                data = yf.download(stock, start=self.start_date, end=self.end_date)
                if not data.empty:
                    self.data_dict[stock] = data
            except Exception as e:
                st.error(f"Failed to download data for {stock}: {str(e)}")

    def analyze_drops(self):
        significant_drops_info = {}
        for stock, data in self.data_dict.items():
            data['Quarterly Change'] = data['Close'].resample('Q').ffill().pct_change()
            significant_drops = data[data['Quarterly Change'] < -0.1]
            drops = [(date, change * 100) for date, change in zip(significant_drops.index, significant_drops['Quarterly Change'])]
            if drops:
                significant_drops_info[stock] = drops
        return significant_drops_info

class Portfolio:
    def __init__(self):
        self.stocks = {}
        self.total_investment = 0

    def add_stock(self, stock, shares, purchase_price):
        """Add stock to the portfolio."""
        self.stocks[stock] = {
            'shares': shares,
            'purchase_price': purchase_price
        }
        self.total_investment += shares * purchase_price

    def calculate_total_value(self, stock_data):
        """Calculate total portfolio value based on current stock prices."""
        total_value = 0
        for stock, details in self.stocks.items():
            if stock in stock_data:
                current_price = stock_data[stock]['Close'].iloc[-1]
                total_value += details['shares'] * current_price
        return total_value

    def calculate_returns(self, stock_data):
        """Calculate total returns and allocation."""
        total_value = self.calculate_total_value(stock_data)
        total_return = total_value - self.total_investment
        allocation = {stock: (details['shares'] * stock_data[stock]['Close'].iloc[-1]) / total_value
                      for stock, details in self.stocks.items() if stock in stock_data}
        return total_return, allocation

# Streamlit User Interface
st.title("Stock Price Analysis and Portfolio Management")
st.sidebar.header("Stock Input")

# Input fields for stock analysis
stocks_input = st.sidebar.text_input("Enter stock symbols (comma-separated):", "NVDA,AAPL,TSLA")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2024-10-01"))

# Input fields for portfolio management
st.sidebar.header("Portfolio Management")
portfolio_input = st.sidebar.text_input("Enter stock symbol and number of shares (e.g., NVDA:10,AAPL:5):")
purchase_price_input = st.sidebar.text_input("Enter purchase price for each stock (e.g., 300,150):")

# Fetch data button
if st.sidebar.button("Fetch Data and Analyze"):
    stocks = [stock.strip().upper() for stock in stocks_input.split(",")]

    # Display the selected stocks
    st.write(f"Analyzing stocks: {stocks}")

    # Create an instance of StockAnalyzer
    analyzer = StockAnalyzer(stocks, start_date, end_date)
    analyzer.fetch_data()

    # Plotting data if any data is available
    if analyzer.data_dict:
        fig = go.Figure()
        for stock, data in analyzer.data_dict.items():
            fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=f'{stock} Closing Price'))
        fig.update_layout(title="Stock Price Comparison", xaxis_title="Date", yaxis_title="Price (USD)")
        st.plotly_chart(fig)

        # Analyze for significant drops
        significant_drops_info = analyzer.analyze_drops()
        if significant_drops_info:
            for stock, drops in significant_drops_info.items():
                st.write(f"\nSignificant drop detected for {stock}:")
                for date, change in drops:
                    st.write(f"- Drop on {date.strftime('%Y-%m-%d')}: {change:.2f}%")
        else:
            st.write("No significant drops detected.")

        # Portfolio management
        if portfolio_input and purchase_price_input:
            try:
                stocks_with_shares = [item.split(':') for item in portfolio_input.split(',')]
                purchase_prices = [float(price) for price in purchase_price_input.split(',')]

                if len(stocks_with_shares) != len(purchase_prices):
                    st.warning("Mismatch between number of stocks and purchase prices.")
                else:
                    portfolio = Portfolio()
                    for (stock_symbol, shares), price in zip(stocks_with_shares, purchase_prices):
                        portfolio.add_stock(stock_symbol.strip().upper(), int(shares), float(price))
                    
                    # Calculate returns and allocation
                    total_return, allocation = portfolio.calculate_returns(analyzer.data_dict)
                    portfolio_value = portfolio.calculate_total_value(analyzer.data_dict)

                if isinstance(portfolio_value, pd.Series):
                    portfolio_value = portfolio_value.sum()

                    st.write(f"Total Portfolio Value: ${portfolio_value:.2f}")

                    st.write(f"Total Portfolio Value: ${portfolio_value:}")
                    st.write(f"Total Return: ${total_return:.2f}")
                    st.write("Portfolio Allocation:")
                    for stock, alloc in allocation.items():
                        st.write(f"- {stock}: {alloc:.2%}")
            except ValueError:
                st.error("Invalid input format. Please enter data in the specified format.")
        else:
            st.warning("Please enter your portfolio information.")
    else:
        st.warning("No valid stock data available for analysis.")

# Alerts functionality
st.sidebar.header("Set Alerts")
alert_stock = st.sidebar.text_input("Enter stock symbol for alert (e.g., AAPL):")
alert_price = st.sidebar.number_input("Enter price threshold for alert:", min_value=0.0)

if st.sidebar.button("Set Alert"):
    if alert_stock and alert_price:
        alert_key = f"{alert_stock.upper()}_ALERT"
        if alert_key in st.session_state:
            st.session_state[alert_key].append(alert_price)
        else:
            st.session_state[alert_key] = [alert_price]
        
        st.success(f"Alert set for {alert_stock.upper()} at price {alert_price:.2f}")
    else:
        st.warning("Please enter stock symbol and price threshold for alert.")

# Notify about price alerts
if hasattr(st.session_state, 'ALERT'):
    for stock, alerts in st.session_state.items():
        if stock.endswith('_ALERT'):
            current_price = analyzer.data_dict.get(stock[:-6])['Close'].iloc[-1] if stock[:-6] in analyzer.data_dict else None
            if current_price is not None:
                for threshold in alerts:
                    if current_price <= threshold:
                        st.warning(f"Alert: {stock[:-6]} has dropped below your threshold of {threshold:.2f}!")
trace = go.Scatter(x=x_data, y=y_data, mode='lines', name='Stock Prices')
fig = go.Figure(data=[trace])
st.plotly_chart(fig)
