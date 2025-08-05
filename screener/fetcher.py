import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_sp500_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    table = soup.find('table', {'id': 'constituents'})
    df = pd.read_html(str(table))[0]
    return df['Symbol'].tolist()

def fetch_stock_data(tickers):
    data = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            data.append({
                "ticker": ticker,
                "pe_ratio": info.get("trailingPE"),
                "market_cap": info.get("marketCap"),
                "price": info.get("currentPrice"),
                "sector": info.get("sector")
            })
        except Exception as e:
            print(f"❌ Error fetching {ticker}: {e}")
    return pd.DataFrame(data)
