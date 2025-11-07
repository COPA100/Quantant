# api docs
# https://ranaroussi.github.io/yfinance/reference/index.html

import yfinance as yf
msft = yf.Ticker("MSFT")


print(msft.get_fast_info()["lastPrice"])