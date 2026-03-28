import pandas as pd
from utils.price import fetch_price_data
from utils.indicators import dma, compute_returns, volume_trend


def compute_features(df: pd.DataFrame) -> pd.DataFrame:
    records = []

    for _, row in df.iterrows():
        symbol = row["symbol"]

        try:
            print(f"\n➡️ Fetching: {symbol}")

            data = fetch_price_data(symbol)

            print(f"✔ Success: {symbol}, rows={len(data)}")

            # Skip if insufficient data
            if data is None or len(data) < 200:
                print(f"⚠️ Skipping (too little data): {symbol}")
                continue

            # --- FIX: Ensure Series (not multi-index DataFrame) ---
            close = data["Close"]
            if isinstance(close, pd.DataFrame):
                close = close.squeeze()

            volume = data["Volume"]
            if isinstance(volume, pd.DataFrame):
                volume = volume.squeeze()

            # --- Compute features safely ---
            price_1y = float(compute_returns(close, 252) or 0)
            price_3y = float(compute_returns(close, len(close)) or 0)

            dma20 = float(dma(close, 20).iloc[-1])
            dma200 = float(dma(close, 200).iloc[-1])

            vol_trend = float(volume_trend(volume))

            records.append({
                "symbol": symbol,
                "price_1y": price_1y,
                "price_3y": price_3y,
                "dma20": dma20,
                "dma200": dma200,
                "volume_trend": vol_trend
            })

        except Exception as e:
            print(f"❌ FAILED: {symbol} → {e}")

    features_df = pd.DataFrame(records)

    # Handle empty case safely
    if features_df.empty:
        print("⚠️ No features computed — check symbol mapping / yfinance")

        df["price_1y"] = None
        df["price_3y"] = None
        df["dma20"] = None
        df["dma200"] = None
        df["volume_trend"] = None

        return df

    return df.merge(features_df, on="symbol", how="left")


def add_signal_flags(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Ensure required columns exist
    for col in ["sales_growth_3y", "profit_growth_3y", "roce"]:
        if col not in df.columns:
            df[col] = 0

    # Ensure numeric safety
    for col in ["price_1y", "price_3y", "volume_trend"]:
        if col not in df.columns:
            df[col] = 0
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Growth signal
    df["growth_flag"] = (
        (df["sales_growth_3y"] > 15) &
        (df["profit_growth_3y"] > 15) &
        (df["roce"] > 12)
    )

    # Consolidation signal
    df["consolidation_flag"] = (
        (df["price_1y"] < 0.25) &
        (df["price_3y"] > 0)
    )

    # Volume accumulation
    df["volume_flag"] = df["volume_trend"] > 1.2

    return df
