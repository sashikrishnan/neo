import pandas as pd


def clean_name(name: str):
    return (
        name.upper()
        .replace(".", "")
        .replace("&", "")
        .replace(",", "")
        .replace("  ", " ")
        .strip()
    )


def load_symbol_map(path="data/symbol_map.csv"):
    df = pd.read_csv(path)

    df["name"] = df["name"].apply(clean_name)
    df["symbol"] = df["symbol"].str.upper().str.strip()

    return dict(zip(df["name"], df["symbol"]))


def map_symbols(df: pd.DataFrame, symbol_map: dict):
    df = df.copy()

    df["name_key"] = df["name"].apply(clean_name)

    # Map
    df["symbol"] = df["name_key"].map(symbol_map)

    # --- DEBUG: Missing mappings ---
    missing_df = df[df["symbol"].isna()].copy()

    if not missing_df.empty:
        print("\n⚠️ Missing symbol mappings (showing first 20):")
        print(missing_df["name"].head(20).to_list())

        # Save detailed debug file
        debug_df = missing_df[["name", "name_key"]].drop_duplicates()

        debug_df.to_csv("outputs/missing_symbols_debug.csv", index=False)

        print("\n➡️ Saved: outputs/missing_symbols_debug.csv")

    # --- DEBUG: Successful mappings ---
    mapped_df = df[df["symbol"].notna()]

    print(f"\n✅ Mapped: {len(mapped_df)} stocks")
    print(f"❌ Missing: {len(missing_df)} stocks")

    # Drop missing (strict mode)
    df = df.dropna(subset=["symbol"])

    df.drop(columns=["name_key"], inplace=True)

    return df
