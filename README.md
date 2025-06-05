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
# Example output:
```
=== Moving Average Crossover Strategy Backtest ===
Stock: MSFT
Period: 2021-01-01 to 2024-01-01
Strategy: 10-day MA crossing 50-day MA
Trade Size: 20 shares per trade

Fetching historical data (this may take a few moments)...
Successfully downloaded 753 days of data

Calculating trading signals...

Strategy Summary:
Short-term MA period: 10 days
Long-term MA period: 50 days
Total days analyzed: 703
Number of buy signals: 9
Number of sell signals: 9

First buy signal: 2021-04-05
Last buy signal: 2023-10-13

Running backtest simulation...
BUY: 2021-04-05 at $249.07 (Cost: $4981.40)
SELL: 2021-05-18 at $243.08 (Profit: $-119.80)
BUY: 2021-06-14 at $259.89 (Cost: $5197.80)
SELL: 2021-09-30 at $281.92 (Profit: $440.60)
BUY: 2021-10-18 at $307.29 (Cost: $6145.80)
SELL: 2022-01-07 at $314.04 (Profit: $135.00)
BUY: 2022-03-28 at $310.70 (Cost: $6214.00)
SELL: 2022-04-18 at $280.52 (Profit: $-603.60)
BUY: 2022-07-28 at $276.41 (Cost: $5528.20)
SELL: 2022-09-02 at $256.06 (Profit: $-407.00)
BUY: 2022-11-18 at $241.22 (Cost: $4824.40)
SELL: 2022-12-30 at $239.82 (Profit: $-28.00)
BUY: 2023-02-01 at $252.75 (Cost: $5055.00)
SELL: 2023-08-04 at $327.78 (Profit: $1500.60)
BUY: 2023-09-14 at $338.70 (Cost: $6774.00)
SELL: 2023-09-20 at $320.77 (Profit: $-358.60)
BUY: 2023-10-13 at $327.73 (Cost: $6554.60)
SELL: 2023-12-29 at $376.04 (Profit: $966.20)

=== Backtest Results ===
💰 Starting Balance: $10,000.00
💰 Final Balance: $11,525.40
📈 Total Return: 15.25%

✅ Total Trades: 9
💵 Total Profit: $1,525.40
📈 Win Rate: 44.44%
📉 Max Drawdown: $1,749.60
💵 Average Profit per Trade: $169.49
🏆 Best Trade: $1,500.60
📉 Worst Trade: $-603.60

=== Strategy Tips ===
• Try different MA periods in config.env:
  - Shorter periods (e.g., 10/30) = more trades, faster response
  - Longer periods (e.g., 50/200) = fewer trades, longer trends
• Adjust trade size (TRADE_QTY) based on your risk tolerance
• Test different stocks to find the best performers
```


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
Create `config/config.env` with your desired parameters:
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
