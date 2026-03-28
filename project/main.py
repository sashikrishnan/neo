from core.loader import load_screener
from core.cleaner import clean_universe
from core.features import compute_features, add_signal_flags
from core.scoring import compute_scores
from core.ranking import rank_stocks
from utils.symbol_mapper import load_symbol_map, map_symbols

# --- AI Layer ---
from ai.sector import load_sector_map, assign_sector, compute_sector_strength
from ai.reasoning import add_reasoning
from ai.macro import load_macro
from ai.scoring import apply_ai_scoring

from core.buy import generate_buy_signals
from core.portfolio import update_portfolio, load_portfolio
from core.sell import generate_sell_signals

def debug_df(stage, df):
    print(f"\n===== {stage} =====")
    print(f"Rows: {len(df)}")

    if len(df) > 0:
        print("Columns:", df.columns.tolist())
        print(df.head(3))
    else:
        print("⚠️ EMPTY DATAFRAME")


def run():
    print("Loading data...")
    df = load_screener("data/screener.csv")
    debug_df("After Load", df)

    print("\nMapping symbols...")
    symbol_map = load_symbol_map("data/symbol_map.csv")
    df = map_symbols(df, symbol_map)
    debug_df("After Symbol Mapping", df)

    print("\nCleaning universe...")
    df = clean_universe(df)
    debug_df("After Cleaning", df)

    print("\nComputing features...")
    df = compute_features(df)
    debug_df("After Feature Engineering", df)

    print("\nAdding signal flags...")
    df = add_signal_flags(df)
    debug_df("After Signal Flags", df)

    # =========================
    # AI LAYER (FREE VERSION)
    # =========================
    print("\nRunning AI layer...")

    sector_map = load_sector_map()
    df = assign_sector(df, sector_map)

    df = compute_sector_strength(df)

    df = add_reasoning(df)

    macro = load_macro()
    df = apply_ai_scoring(df, macro)

    debug_df("After AI Layer", df)

    print("\nScoring...")
    df = compute_scores(df)
    debug_df("After Scoring", df)

    print("\nRanking...")
    df = rank_stocks(df)
    debug_df("After Ranking", df)

    df.to_csv("outputs/final_ranked.csv", index=False)

    print("\n✅ Done. Output: outputs/final_ranked.csv")

    print("\nGenerating BUY signals...")
    buy_df = generate_buy_signals(df)
    print(buy_df)

    buy_df.to_csv("outputs/buy_signals.csv", index=False)

    update_portfolio(buy_df)

    print("\nGenerating SELL signals...")
    portfolio = load_portfolio()
    sell_df = generate_sell_signals(df, portfolio)

    if not sell_df.empty:
        print(sell_df)
        sell_df.to_csv("outputs/sell_signals.csv", index=False)
    else:
        print("No SELL signals")

if __name__ == "__main__":
    run()
