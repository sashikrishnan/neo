import pandas as pd


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.replace("\n", " ")
        .str.replace(".", "", regex=False)
        .str.replace("%", "pct")
        .str.replace("\xa0", "")   # fix non-breaking spaces
        .str.replace(" ", "_")
        .str.lower()
    )
    return df


def load_screener(path="data/screener.csv") -> pd.DataFrame:
    df = pd.read_csv(path)

    # Normalize column names
    df = normalize_columns(df)

    print("\nColumns detected:")
    print(df.columns.tolist())

    # --- BASIC RENAME (ONLY SAFE ONES) ---
    rename_map = {
        "name": "name",
        "mar_caprscr": "market_cap",
    }

    df = df.rename(columns=rename_map)

    # --- FORCE CORRECT VALUE EXTRACTION (FINAL FIX) ---

    # Growth
    if "sales_var_3yrspct" in df.columns:
        df["sales_growth_3y"] = pd.to_numeric(df["sales_var_3yrspct"], errors="coerce")

    if "profit_var_3yrspct" in df.columns:
        df["profit_growth_3y"] = pd.to_numeric(df["profit_var_3yrspct"], errors="coerce")

    # ROCE
    if "rocepct" in df.columns:
        df["roce"] = pd.to_numeric(df["rocepct"], errors="coerce")

    # Sales
    if "sales_qtrrscr" in df.columns:
        df["sales"] = pd.to_numeric(df["sales_qtrrscr"], errors="coerce")

    # --- ENSURE NUMERIC TYPES ---
    numeric_cols = [
        "market_cap",
        "sales_growth_3y",
        "profit_growth_3y",
        "roce",
        "sales"
    ]

    for col in numeric_cols:
        if col not in df.columns:
            df[col] = 0
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # --- DROP ONLY BAD NAME ROWS ---
    df = df.dropna(subset=["name"])

    # --- REQUIRED DEFAULTS ---
    if "symbol" not in df.columns:
        df["symbol"] = df["name"]

    if "debt" not in df.columns:
        df["debt"] = 0.0

    if "promoter_holding" not in df.columns:
        df["promoter_holding"] = 50.0

    return df.reset_index(drop=True)
