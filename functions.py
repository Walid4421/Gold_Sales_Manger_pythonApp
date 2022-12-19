# getting gold price from  http://www.exchangerates.org.uk/commodities/live-gold-prices/XAU-USD.html using https://github.com/Nirajkashyap/live_stock_price/blob/5d226e23fad285d0303838dcf4d46249674ca06a/gold.py
import re
import urllib.request
# Api used to get conversion rate of the turkish lira from openexchangerate
from openexchangerate import OpenExchangeRates

client = OpenExchangeRates(api_key="8419ea072d454514bb4d179fb94adb78")

nae = 0.00

for name, price in client:  # Iterator support.
    if name == "TRY":
        nae = float(price)
        print(nae)


gold_rate = False # this is set to keep in track if the app got the rate for the gold

ur = urllib.request.urlopen('http://www.exchangerates.org.uk/commodities/live-gold-prices/XAU-USD.html')

html = ur.read().decode('utf-8')

str1 = re.search("value_XAUUSD", html, re.I)

if str1:

    index_val = html.index("value_XAUUSD")
    index_val_update = index_val + 14
    index_val_update_end = index_val + 23
    gold_rate = True  # if it got the Gold rate it would assign true to the gold rate
    print(float(html[index_val_update: index_val_update_end])/31.1034768)


else:
    gold_rate = False   # else it would assign false
