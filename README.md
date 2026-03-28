# 📈 NEO - AI-Enhanced Stock Ranking & Trading System

## 🚀 Overview

NEO is a Python-based stock analysis and trading system designed for Indian markets.

It combines:
- Factor-based scoring
- Technical signals
- AI-inspired contextual adjustments (sector, macro, reasoning)

The system ranks stocks, generates BUY/SELL signals, and maintains a portfolio.

---

## 🧠 System Architecture

Pipeline:
Data → Cleaning → Features → Signals → AI Layer → Scoring → Ranking → Buy/Sell → Portfolio

---

## ⚙️ Core Features

### 📊 Data Processing
- Loads screener data (`data/screener.csv`)
- Maps symbols using `symbol_map.csv`

### 🧹 Data Cleaning
- Filters and cleans stock universe
- Removes invalid/undesired entries

### 📉 Feature Engineering
- Price-based features
- Technical indicators (via `utils/indicators.py`)

### 🚦 Signal Flags
- Pre-signal indicators used for BUY/SELL logic

---

## 🤖 AI Layer (Key Differentiator)

Located in `ai/`:

### 🔹 Sector Intelligence
- Assigns sector (`sector.py`)
- Computes sector strength

### 🔹 Macro Overlay
- Macro conditions influence scoring (`macro.py`)

### 🔹 Reasoning Layer
- Adds explainability to signals (`reasoning.py`)

### 🔹 AI Scoring Adjustment
- Adjusts base scores dynamically (`ai/scoring.py`)

---

## 📊 Scoring & Ranking

Located in `core/`:

- `scoring.py` → computes final score
- `ranking.py` → ranks stocks
- Output:
outputs/final_ranked.csv


---

## 🟢 Buy System

- File: `core/buy.py`
- Generates BUY signals based on:
- Ranking
- Signals
- AI adjustments

Output:
outputs/buy_signals.csv


---

## 🔴 Sell System

- File: `core/sell.py`
- Uses:
  - Portfolio data
  - Current signals

Output:
outputs/sell_signals.csv


---

## 💼 Portfolio Management

- File: `core/portfolio.py`
- Tracks active positions
- Stored in:
data/portfolio.json


---

## 🏗️ Project Structure

neo/
│
├── main.py # Entry point
│
├── core/ # Core pipeline
│ ├── loader.py
│ ├── cleaner.py
│ ├── features.py
│ ├── scoring.py
│ ├── ranking.py
│ ├── buy.py
│ ├── sell.py
│ ├── portfolio.py
│
├── ai/ # AI enhancement layer
│ ├── sector.py
│ ├── macro.py
│ ├── reasoning.py
│ ├── scoring.py
│
├── utils/
│ ├── indicators.py
│ ├── price.py
│ ├── symbol_mapper.py
│
├── data/
│ ├── screener.csv
│ ├── symbol_map.csv
│ ├── portfolio.json
│ ├── sector_map.json
│ ├── exclusion_list.csv
│
├── outputs/ # Generated results (ignored in git)
│
├── doc/ # Strategy & system design PDFs
│
├── requirements.txt
└── README.md


---

## ▶️ How It Works

Run:

```bash
python main.py

Steps executed:

- Load screener data
- Map symbols
- Clean universe
- Compute features
- Add signal flags
- Run AI layer
- Compute scores
- Rank stocks
- Generate BUY signals
- Update portfolio
- Generate SELL signals

📁 Key Outputs
File	Description
- final_ranked.csv	Ranked stock universe
- buy_signals.csv	Stocks to buy
- sell_signals.csv	Stocks to sell

📚 Documentation
Located in /doc:
- Multibagger strategy blueprints
- Ranking system design
- Full system architecture references

🔮 Roadmap
 Backtesting engine
 Paper trading simulation
 Broker API integration
 Web dashboard
 AI model-based scoring (ML instead of rules)

⚠️ Disclaimer
This project is for educational purposes only.
Not financial advice.

👤 Author
Sashi Krishnan
