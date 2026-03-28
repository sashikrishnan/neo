import json
import os
from datetime import datetime

PORTFOLIO_FILE = "data/portfolio.json"


def load_portfolio():
    # --- If file doesn't exist ---
    if not os.path.exists(PORTFOLIO_FILE):
        return []

    # --- If file is empty ---
    if os.path.getsize(PORTFOLIO_FILE) == 0:
        return []

    try:
        with open(PORTFOLIO_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Portfolio read error: {e}")
        return []


def save_portfolio(data):
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(data, f, indent=2)


def update_portfolio(buy_df):
    portfolio = load_portfolio()

    existing_symbols = {p["symbol"] for p in portfolio}

    for _, row in buy_df.iterrows():
        symbol = row["symbol"]

        # --- Avoid duplicate buys ---
        if symbol in existing_symbols:
            continue

        portfolio.append({
            "symbol": symbol,
            "buy_price": row.get("cmprs", 0),  # FIX: correct column
            "buy_date": datetime.today().strftime("%Y-%m-%d")
        })

    save_portfolio(portfolio)

    print(f"Portfolio updated: {len(portfolio)} holdings")
