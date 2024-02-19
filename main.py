import numpy as np
import pandas as pd
import yfinance as yf

# Data Analysis
def fetch_data(ticker, period='1y', interval='1d'):
    """
    Fetch historical data for a given ticker symbol from Yahoo Finance.
    """
    data = yf.download(ticker, period=period, interval=interval)
    return data

def calculate_moving_averages(data, short_window=20, long_window=50):
    """
    Calculate short-term and long-term moving averages.
    """
    data['SMA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['LMA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    return data

# Trading Algorithm
def crossover_strategy(data):
    """
    A simple moving average crossover strategy.
    Buy when the short moving average crosses above the long moving average.
    Sell when the short moving average crosses below the long moving average.
    """
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['signal'][short_window:] = np.where(data['SMA'][short_window:] 
                                                > data['LMA'][short_window:], 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals

# Risk Management
def apply_risk_management(signals, data, capital, risk_per_trade=0.01):
    """
    Apply risk management to limit the size of trades based on volatility.
    """
    signals['volatility'] = data['Close'].pct_change().rolling(window=20).std()
    signals['trade_size'] = capital * risk_per_trade / signals['volatility']
    signals['trade_size'].fillna(0, inplace=True)
    return signals

# Main execution
if __name__ == "__main__":
    # Parameters
    ticker = 'AAPL'
    capital = 10000  # Capital to trade
    short_window = 20
    long_window = 50
    
    # Fetch and process data
    data = fetch_data(ticker)
    data_with_ma = calculate_moving_averages(data, short_window, long_window)
    
    # Generate trading signals
    trading_signals = crossover_strategy(data_with_ma)
    
    # Apply risk management
    trading_signals_with_risk = apply_risk_management(trading_signals, data_with_ma, capital)
    
    # Print results
    print(trading_signals_with_risk.tail())
