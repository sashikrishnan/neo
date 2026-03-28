import pandas as pd


def rank_stocks(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df.sort_values("final_score", ascending=False)

    df["rank"] = range(1, len(df) + 1)

    return df
