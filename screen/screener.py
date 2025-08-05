def filter_stocks(df):
    # Only keep stocks with:
    # - P/E < 20
    # - Market Cap > $10B
    # - Price between $10 and $500
    filtered = df[
        (df["pe_ratio"] < 20) &
        (df["market_cap"] > 10e9) &
        (df["price"] > 10) &
        (df["price"] < 500)
    ]
    return filtered.dropna()
