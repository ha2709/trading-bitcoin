import pandas as pd
import matplotlib.pyplot as plt
import ccxt

# Initialize exchange
exchange = ccxt.binance()

# Fetch historical OHLCV data
symbol = 'BTC/USDT'
timeframe = '1d'
since = exchange.parse8601('2022-01-01T00:00:00Z')
ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since)
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(df['timestamp'], df['close'], label='Bitcoin Price')
plt.title('Bitcoin Price Trend')
plt.xlabel('Date')
plt.ylabel('Price in USDT')
plt.legend()
plt.show()
