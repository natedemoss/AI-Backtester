import pandas as pd
import numpy as np

def calculate_signals(data: pd.DataFrame, fast_period: int, slow_period: int) -> pd.DataFrame:
    """
    Calculate simple moving average (SMA) signals for trading.
    
    Strategy Explanation:
    - When the short-term average (fast SMA) goes above the long-term average (slow SMA), it's a buy signal
    - When the short-term average goes below the long-term average, it's a sell signal
    - This strategy follows the trend: buy when price is trending up, sell when trending down
    
    Args:
        data (pd.DataFrame): DataFrame with OHLCV data
        fast_period (int): Number of days for the short-term average (e.g., 20 days)
        slow_period (int): Number of days for the long-term average (e.g., 50 days)
    
    Returns:
        pd.DataFrame: DataFrame with added signal columns
    """
    # Calculate the moving averages
    data['Short_MA'] = data['Close'].rolling(window=fast_period).mean()
    data['Long_MA'] = data['Close'].rolling(window=slow_period).mean()
    
    # Calculate previous day's values for crossover detection
    data['Short_MA_Prev'] = data['Short_MA'].shift(1)
    data['Long_MA_Prev'] = data['Long_MA'].shift(1)
    
    # Initialize signal column
    data['signal'] = 0
    
    # Generate signals
    # Buy when short MA crosses above long MA
    buy_condition = (data['Short_MA'] > data['Long_MA']) & (data['Short_MA_Prev'] <= data['Long_MA_Prev'])
    # Sell when short MA crosses below long MA
    sell_condition = (data['Short_MA'] < data['Long_MA']) & (data['Short_MA_Prev'] >= data['Long_MA_Prev'])
    
    # Set signals
    data.loc[buy_condition, 'signal'] = 1    # 1 means buy
    data.loc[sell_condition, 'signal'] = -1  # -1 means sell
    
    # Remove NaN values
    data = data.dropna()
    
    # Print strategy summary
    print(f"\nStrategy Summary:")
    print(f"Short-term MA period: {fast_period} days")
    print(f"Long-term MA period: {slow_period} days")
    print(f"Total days analyzed: {len(data)}")
    print(f"Number of buy signals: {len(data[data['signal'] == 1])}")
    print(f"Number of sell signals: {len(data[data['signal'] == -1])}")
    
    if len(data[data['signal'] == 1]) > 0:
        print(f"\nFirst buy signal: {data[data['signal'] == 1].index[0].date()}")
        print(f"Last buy signal: {data[data['signal'] == 1].index[-1].date()}")
    
    return data 