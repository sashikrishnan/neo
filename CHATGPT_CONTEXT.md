# 🤖 CHATGPT CONTEXT - NEO PROJECT

## 📌 Purpose
This file provides context for ChatGPT to quickly understand the project without needing full code ingestion.

---

## 🧠 Project Summary

NEO is an AI-enhanced stock ranking and trading system for Indian markets.

Pipeline:
Data → Cleaning → Features → Signals → AI Layer → Scoring → Ranking → Buy/Sell → Portfolio

---

## 🏗️ Key Modules

### core/
- loader.py → loads screener data
- cleaner.py → filters stocks
- features.py → computes features
- scoring.py → base scoring
- ranking.py → ranking logic
- buy.py → buy signals
- sell.py → sell signals
- portfolio.py → tracks holdings

### ai/
- sector.py → sector classification
- macro.py → macro overlay
- reasoning.py → explanation layer
- scoring.py → score adjustments

### utils/
- indicators.py → RSI, MACD, EMA
- price.py → price utilities
- symbol_mapper.py → mapping

---

## 📁 Data Files

- data/screener.csv
- data/symbol_map.csv
- data/portfolio.json
- data/sector_map.json
- data/exclusion_list.csv

---

## 📊 Outputs

- outputs/final_ranked.csv
- outputs/buy_signals.csv
- outputs/sell_signals.csv

(outputs folder is ignored in git)

---

## ▶️ How to Run

```bash
python main.py
