def classify_reason(row):
    if row["growth_flag"] and row["consolidation_flag"]:
        return "undervalued_growth"

    if not row["growth_flag"]:
        return "no_growth"

    if row["price_1y"] > 0.6:
        return "already_moved"

    if row["volume_trend"] < 1:
        return "no_accumulation"

    return "neutral"


def add_reasoning(df):
    df = df.copy()
    df["ai_reason"] = df.apply(classify_reason, axis=1)
    return df
