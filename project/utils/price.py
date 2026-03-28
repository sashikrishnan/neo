import yfinance as yf


def format_symbol(symbol: str) -> str:
    symbol = symbol.strip().upper()

    if symbol.endswith(".NS"):
        return symbol

    return f"{symbol}.NS"


def fetch_price_data(symbol: str, period="3y"):
    symbol = symbol.strip().upper()

    # DO NOT append .NS anymore
    data = yf.download(symbol, period=period, progress=False)

    if data is None or data.empty:
        raise ValueError(f"No data for {symbol}")

    data.dropna(inplace=True)
    return data
