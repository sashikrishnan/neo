import pandas as pd
import json


def load_sector_map(path="data/sector_map.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}


def assign_sector(df, sector_map):
    df = df.copy()

    symbol_to_sector = {}
    for sector, symbols in sector_map.items():
        for s in symbols:
            symbol_to_sector[s] = sector

    df["sector"] = df["symbol"].map(symbol_to_sector).fillna("Unknown")

    return df


def compute_sector_strength(df):
    sector_perf = df.groupby("sector")["price_1y"].mean().to_dict()

    def classify(sector):
        if sector == "Unknown":
            return "neutral"   # ✅ FIX

        val = sector_perf.get(sector, 0)

        if val > 0.5:
            return "strong"
        elif val > 0.2:
            return "improving"
        else:
            return "weak"

    df["sector_strength"] = df["sector"].apply(classify)
    return df
