#!/bin/bash

mkdir -p project/{data,core,ai,trading,utils,outputs}

touch project/main.py

# data
touch project/data/screener.csv
touch project/data/sector_map.json
touch project/data/portfolio.json

# core
touch project/core/{loader.py,cleaner.py,features.py,scoring.py,ranking.py}

# ai
touch project/ai/{sector.py,reasoning.py,scoring.py}

# trading
touch project/trading/{buy.py,sell.py,portfolio.py}

# utils
touch project/utils/{price.py,indicators.py}

echo "Project structure created"
