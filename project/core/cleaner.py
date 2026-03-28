import pandas as pd


def load_exclusion_list(path="data/exclusion_list.csv"):
    try:
        df = pd.read_csv(path)

        # Remove comments / empty rows
        df = df[df["symbol"].notna()]
        df["symbol"] = df["symbol"].astype(str).str.strip().str.upper()

        return set(df["symbol"])
    except Exception as e:
        print(f"⚠️ Could not load exclusion list: {e}")
        return set()


def clean_universe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    initial_count = len(df)

    # --- Manual exclusion only ---
    exclude_symbols = load_exclusion_list()

    if not exclude_symbols:
        print("⚠️ No exclusions applied")
        return df.reset_index(drop=True)

    removed_df = df[df["symbol"].str.upper().isin(exclude_symbols)].copy()
    removed_df["reason"] = "manual"

    df = df[~df["symbol"].str.upper().isin(exclude_symbols)]

    # --- Save removed ---
    if not removed_df.empty:
        removed_df = removed_df[["name", "symbol", "reason"]].drop_duplicates()
        removed_df.to_csv("outputs/removed_symbols.csv", index=False)

        print(f"Removed (manual): {len(removed_df)} → saved to outputs/removed_symbols.csv")

    final_count = len(df)

    print(f"Initial universe: {initial_count}")
    print(f"Final universe: {final_count}")

    return df.reset_index(drop=True)
