import pandas as pd
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator
from ta.momentum import StochasticOscillator
from ta.trend import EMAIndicator
from ta.trend import MACD

btc_table = pd.read_csv('../data/CRYPTO_DATA_15M_BTC(1000)3.csv')

indicator_12EMA = EMAIndicator(close=btc_table["nsClosePrice"], window=12, fillna=True)
btc_table['12EMA'] = indicator_12EMA.ema_indicator()
indicator_26EMA = EMAIndicator(close=btc_table["nsClosePrice"], window=26, fillna=True)
btc_table['26EMA'] = indicator_26EMA.ema_indicator()


indicator_macd = MACD(close=btc_table["nsClosePrice"], window_slow=26, window_fast=12, window_sign=9)
btc_table['trend_macd'] = indicator_macd.macd()
btc_table['trend_macd_signal'] = indicator_macd.macd_signal()
btc_table['trend_macd_diff'] = indicator_macd.macd_diff()

indicator_rsi = RSIIndicator(close=btc_table["nsClosePrice"], window=14)
btc_table['momentum_rsi'] = indicator_rsi.rsi()

indicator_stoc = StochasticOscillator(high=btc_table["nsHighPrice"], low=btc_table["nsLowPrice"],
                                      close=btc_table["nsClosePrice"], window=14, smooth_window=3)
btc_table['momentum_stoch'] = indicator_stoc.stoch()
btc_table['momentum_stoch'] = indicator_stoc.stoch()

indicator_bb = BollingerBands(close=btc_table["nsClosePrice"], window=20, window_dev=2)
btc_table['volatility_bbh'] = indicator_bb.bollinger_hband()
btc_table['volatility_bbl'] = indicator_bb.bollinger_lband()
btc_table['volatility_wid'] = indicator_bb.bollinger_hband() - indicator_bb.bollinger_lband()

df = btc_table.loc[:100 ,
     ['nsYMD','nsMACD','trend_macd','nsMACD_SIGNAL', 'trend_macd_signal',
      'nsEMA12','12EMA','nsEMA26','26EMA',
      'nsMACD_OSC', 'trend_macd_diff',
      'nsRSI', 'momentum_rsi',
      'nsSTO_K', 'momentum_stoch',
      'nsSTO_D',
      'nsBOL_UP', 'volatility_bbh',
      'nsBOL_DOWN', 'volatility_bbl',
      'nsBOL_WIDTH', 'volatility_wid'
      ]]

print(df.to_string())
