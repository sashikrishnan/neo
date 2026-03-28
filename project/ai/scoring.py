from ai.macro import macro_adjustment


def compute_ai_score(row, macro):
    score = 0.5

    # Reason logic
    if row["ai_reason"] == "undervalued_growth":
        score = 1.0
    elif row["ai_reason"] == "no_growth":
        score -= 0.4
    elif row["ai_reason"] == "already_moved":
        score -= 0.2
    elif row["ai_reason"] == "no_accumulation":
        score -= 0.2

    # Sector strength
    if row["sector_strength"] == "strong":
        score += 0.2
    elif row["sector_strength"] == "improving":
        score += 0.1
    elif row["sector_strength"] == "weak":
        score -= 0.2

    # Macro overlay
    score += macro_adjustment(row, macro)

    return max(0, min(score, 1))


def apply_ai_scoring(df, macro):
    df = df.copy()
    df["ai_score"] = df.apply(lambda r: compute_ai_score(r, macro), axis=1)
    return df
