import pandas as pd


def normalize(series: pd.Series) -> pd.Series:
    if series.max() == series.min():
        return pd.Series([0.5] * len(series), index=series.index)

    return (series - series.min()) / (series.max() - series.min())


def compute_scores(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # --- Fundamental Score (ROCE) ---
    df["fundamental_score"] = normalize(df["roce"])

    # --- Growth Score ---
    growth_raw = (
        0.5 * df["sales_growth_3y"] +
        0.5 * df["profit_growth_3y"]
    )
    df["growth_score"] = normalize(growth_raw)

    # --- Consolidation Score ---
    df["consolidation_score"] = normalize(1 - df["price_1y"])

    # --- Volume Score ---
    df["volume_score"] = normalize(df["volume_trend"])

    # --- Final Score (AI already computed earlier) ---
    df["final_score"] = (
        0.4 * df["fundamental_score"] +
        0.2 * df["growth_score"] +
        0.2 * df["consolidation_score"] +
        0.1 * df["volume_score"] +
        0.1 * df["ai_score"]
    )

    return df
