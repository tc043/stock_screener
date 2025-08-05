import os
from screener.fetcher import get_sp500_tickers, fetch_stock_data
from screener.screener import filter_stocks
from screener.storage import save_to_db

def run():
    print("📡 Loading S&P 500 tickers...")
    tickers = get_sp500_tickers()

    print(f"📈 Fetching data for {len(tickers)} tickers...")
    df = fetch_stock_data(tickers)

    print("🔍 Applying filters...")
    filtered = filter_stocks(df)

    print(f"✅ {len(filtered)} stocks passed filters")
    
    os.makedirs("data", exist_ok=True)
    save_to_db(filtered)
    print("💾 Data saved to database")

if __name__ == "__main__":
    run()
