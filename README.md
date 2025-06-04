# Backtesting Bot

A simple command-line backtesting tool that implements a SMA crossover strategy.

## Features

- Fetches historical stock data using yfinance
- Implements SMA crossover strategy
- Simulates trades at closing prices
- Calculates key performance metrics:
  - Total profit/loss
  - Number of trades
  - Win rate
  - Maximum drawdown

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the strategy:
Edit `config/config.env` with your desired parameters:
```
TICKER=AAPL
START_DATE=2020-01-01
END_DATE=2024-01-01
SMA_FAST=50
SMA_SLOW=200
TRADE_QTY=10
```

## Usage

Run the backtest:
```bash
python main.py
```

## Strategy Logic

- Buy when fast SMA crosses above slow SMA
- Sell when fast SMA crosses below slow SMA
- All trades execute at closing prices
- Fixed position size per trade

## Project Structure

```
backtest_bot/
│
├── config/
│   └── config.env              # User parameters
│
├── data/
│   └── fetch_data.py           # Data fetching
│
├── strategy/
│   └── sma_crossover.py        # Strategy implementation
│
├── backtest/
│   └── backtester.py           # Backtesting engine
│
├── main.py                     # Main script
├── requirements.txt
└── README.md
``` 