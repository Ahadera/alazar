import os
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import requests
import streamlit as st

# Dictionary for cross-referencing related words
related_words = {
    'crash': ['plummet', 'collapse', 'fall', 'slump'],
    'decline': ['drop', 'dip', 'fall', 'decrease'],
    'plunge': ['nosedive', 'sink', 'tumble', 'dive'],
    'sell-off': ['panic selling', 'liquidation', 'dumping']
}

def is_relevant_article(title, description):
    """Checks if the article title or description contains any related words."""
    for key_word, synonyms in related_words.items():
        # Check if the key word or any synonym appears in the title or description
        if any(word in title.lower() or word in description.lower() for word in [key_word] + synonyms):
            return True
    return False

# Function to get news articles
def get_news(stock, start_date, end_date):
    api_key = '79b9054b6ab142b28ed95fce9ef47423'  # Replace with your NewsAPI key
    url = f'https://newsapi.org/v2/everything?q={stock}&from={start_date}&to={end_date}&sortBy=relevance&apiKey={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        if news_data['status'] == 'ok':
            articles = news_data['articles']
            relevant_articles = []
            for article in articles[:5]:  # Display the top 5 articles
                title = article['title']
                description = article.get('description', '')

                # Cross-reference with related words
                if is_relevant_article(title, description):
                    relevant_articles.append(f"- {title} ({article['source']['name']})\n  {article['url']}")
            return relevant_articles
        else:
            return [f"Failed to get news for {stock}: {news_data.get('message', 'No message available')}"]
    else:
        return [f"Request failed with status code: {response.status_code}"]

# Streamlit User Interface
st.title("Stock Price Analysis and News Relevance")
st.sidebar.header("Stock Input")

# Input fields
stocks_input = st.sidebar.text_input("Enter stock symbols (comma-separated):", "NVDA,AAPL,TSLA")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2024-10-01"))

# Fetch data button
if st.sidebar.button("Fetch Data and Analyze"):
    stocks = [stock.strip().upper() for stock in stocks_input.split(",")]

    # Display the selected stocks
    st.write(f"Analyzing stocks: {stocks}")

    # Download stock data
    data_dict = {}
    for stock in stocks:
        try:
            data = yf.download(stock, start=start_date, end=end_date)
            if data.empty:
                st.warning(f"No data found for {stock}.")
            else:
                data_dict[stock] = data
        except Exception as e:
            st.error(f"Failed to download data for {stock}: {str(e)}")

    # Plotting data if any data is available
    if data_dict:
        fig = go.Figure()
        for stock, data in data_dict.items():
            fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=f'{stock} Closing Price'))
        fig.update_layout(title="Stock Price Comparison", xaxis_title="Date", yaxis_title="Price (USD)")
        st.plotly_chart(fig)

        # Analyze for significant drops and display news
        for stock, data in data_dict.items():
            if not isinstance(data.index, pd.DatetimeIndex):
                data.index = pd.to_datetime(data.index)

            data['Quarterly Change'] = data['Close'].resample('Q').ffill().pct_change()
            significant_drops = data[data['Quarterly Change'] < -0.1]

            if not significant_drops.empty:
                st.write(f"\nSignificant drop detected for {stock}:")
                for date in significant_drops.index:
                    st.write(f"- Drop on {date.strftime('%Y-%m-%d')}: {significant_drops.loc[date, 'Quarterly Change']*100:.2f}%")
                    start_date_str = (date - pd.DateOffset(months=3)).strftime('%Y-%m-%d')
                    end_date_str = date.strftime('%Y-%m-%d')

                    # Fetch and display relevant news
                    news_articles = get_news(stock, start_date_str, end_date_str)
                    if news_articles:
                        st.write(f"Relevant news articles for {stock} from {start_date_str} to {end_date_str}:")
                        for article in news_articles:
                            st.markdown(article, unsafe_allow_html=True)
                    else:
                        st.write(f"No relevant news articles found for {stock} on {date.strftime('%Y-%m-%d')}.")
    else:
        st.warning("No valid stock data available for analysis.")
