import pandas as pd


def generate_sell_signals(df: pd.DataFrame, portfolio: list):
    df = df.copy()

    sell_signals = []

    for stock in portfolio:
        symbol = stock["symbol"]
        buy_price = stock["buy_price"]

        row = df[df["symbol"] == symbol]

        if row.empty:
            continue

        row = row.iloc[0]
        current_price = row.get("cmprs", 0)

        if current_price == 0:
            continue

        change = (current_price - buy_price) / buy_price

        # --- SELL RULES ---
        if change <= -0.03:
            reason = "stop_loss"

        elif row["consolidation_flag"] == False:
            reason = "trend_break"

        elif row["price_1y"] > 1.5:
            reason = "profit_booking"

        else:
            continue

        sell_signals.append({
            "symbol": symbol,
            "action": "SELL",
            "reason": reason,
            "return_pct": round(change * 100, 2)
        })

    return pd.DataFrame(sell_signals)
