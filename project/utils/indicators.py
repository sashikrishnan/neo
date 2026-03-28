import pandas as pd


def dma(series: pd.Series, window: int):
    return series.rolling(window).mean()


def compute_returns(series: pd.Series, days: int):
    if len(series) < days:
        return None
    return (series.iloc[-1] / series.iloc[-days]) - 1


def volume_trend(volume: pd.Series, window=60):
    return volume.tail(window).mean() / volume.tail(window * 2).mean()
