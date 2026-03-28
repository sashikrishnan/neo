import json


def load_macro(path="data/macro.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}


def macro_adjustment(row, macro):
    adj = 0

    # Market trend
    if macro.get("market_trend") == "bull":
        adj += 0.05
    elif macro.get("market_trend") == "bear":
        adj -= 0.1

    # Crude impact
    if macro.get("crude_trend") == "rising":
        if row["sector"] == "Energy":
            adj += 0.05
        if row["sector"] == "Consumer":
            adj -= 0.05

    # Interest rate
    if macro.get("interest_rate") == "high":
        if row["sector"] in ["Real Estate", "Finance"]:
            adj -= 0.05

    return adj
