# 🤖 CHATGPT CONTEXT - NEO PROJECT

## 📌 Project Summary

NEO is an AI-enhanced stock ranking and trading system for Indian markets.

It combines:

* Factor-based scoring
* Technical indicators
* AI-inspired contextual adjustments (sector, macro, reasoning)

Pipeline:
Data → Cleaning → Features → Signals → AI Layer → Scoring → Ranking → Buy/Sell → Portfolio

---

## 🏗️ Architecture

The system follows a modular pipeline design:

* **core/** → main pipeline execution
* **ai/** → contextual intelligence layer
* **utils/** → reusable utilities
* **data/** → input datasets & portfolio state
* **outputs/** → generated results (ignored in git)

Execution flow:

1. Load data
2. Clean universe
3. Generate features
4. Compute signals
5. Apply AI adjustments
6. Score & rank
7. Generate buy/sell
8. Update portfolio

---

## ⚙️ Key Modules

### core/

* loader.py → loads screener data
* cleaner.py → filters stocks
* features.py → feature engineering
* scoring.py → base scoring
* ranking.py → ranking logic
* buy.py → buy signal generation
* sell.py → sell signal generation
* portfolio.py → portfolio tracking

### ai/

* sector.py → sector classification
* macro.py → macro conditions overlay
* reasoning.py → explainability layer
* scoring.py → AI-based score adjustments

### utils/

* indicators.py → RSI, MACD, EMA
* price.py → price utilities
* symbol_mapper.py → symbol mapping

---

## 📁 Data & Outputs

### Data (tracked)

* data/screener.csv
* data/symbol_map.csv
* data/portfolio.json
* data/sector_map.json
* data/exclusion_list.csv

### Outputs (ignored)

* outputs/final_ranked.csv
* outputs/buy_signals.csv
* outputs/sell_signals.csv

---

## 🚀 Current State

* End-to-end pipeline working
* AI layer integrated with scoring
* Portfolio tracking implemented
* Repo cleaned (removed unused trading module)
* `.gitignore` properly configured
* Context generation script (`generate_context.sh`) working
* README and context system established

---

## 🧠 Known Constraints / Decisions

* Outputs are **not tracked** (ephemeral, reproducible)
* Data is **tracked** (important for reproducibility & testing)
* AI layer enhances rule-based system (not ML model yet)
* Modular separation must be maintained (core vs ai vs utils)
* Avoid duplicate logic across modules

---

## 🔧 Active Focus

* Improve system robustness and structure
* Prepare for automation (GitHub Actions)
* Future: add backtesting engine

---

## 🧾 Session Updates (APPEND ONLY)

### Session 2026-03-28

* Added GitHub repo and configured SSH access
* Implemented `.gitignore` and cleaned repo (removed venv, outputs)
* Created `generate_context.sh` for reproducible project snapshots
* Added README.md (project documentation)
* Added CHATGPT_CONTEXT.md (AI context system)
* Removed unused `trading/` module
* Established generational workflow for context evolution

---

