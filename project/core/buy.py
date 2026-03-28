import pandas as pd
from datetime import datetime

def generate_buy_signals(df: pd.DataFrame, top_n=10):
    df = df.copy()

    buy_df = df[
        (df["growth_flag"] == True) &
        (df["consolidation_flag"] == True) &
        (df["price_1y"] < 0.8)
    ]

    buy_df = buy_df.sort_values("final_score", ascending=False).head(top_n)

    buy_df["action"] = "BUY"
    buy_df["date"] = datetime.today().strftime("%Y-%m-%d")

    return buy_df[[
        "symbol", "name", "cmprs",   # ✅ ADD THIS
        "final_score", "price_1y", "ai_score", "sector",
        "action", "date"
    ]]
