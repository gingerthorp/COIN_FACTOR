import pandas as pd
from ta import add_all_ta_features

btc_table = pd.read_csv('../data/CRYPTO_15M_BTC.csv')

print(btc_table)

btc_table = add_all_ta_features(btc_table,
                                open="nsOpenPrice", high="nsHighPrice", low="nsLowPrice", close="nsClosePrice", volume="nsTradeQty")

print(btc_table)

btc_table.to_csv("../data/vf_CRYPTO_15M_BTC.csv")