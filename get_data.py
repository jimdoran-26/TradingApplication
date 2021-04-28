from yahoo_fin import stock_info as si
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

#GET PRICE AND RETURN DATA ACROSS A RANGE OF DATES
def price_grab(ticker,start_date,end_date):
    stock = pd.DataFrame()

    if isinstance(ticker,str):
        stock[ticker] = wb.DataReader(ticker, data_source='yahoo', start=start_date, end=end_date)['Adj Close']
    else:
        for i in ticker:
            stock[i] = wb.DataReader(i, data_source='yahoo', start=start_date, end=end_date)['Adj Close']
    return stock

def returns_grab(ticker,start_date,end_date):
    prices = price_grab(ticker,start_date,end_date)
    # calculate returns
    returns = pd.DataFrame()
    for i in prices:
        returns[i] = (prices[i] / prices[i].shift(1)) - 1

    # cumulative returns
    cum_return = pd.DataFrame()
    for j in returns:
        cum_return[j] = 100 * (np.exp(np.log1p(returns[j]).cumsum()) - 1)

    return cum_return


#GET THE CURRENT PRICE OF STOCK/STOCKS
def return_current_price(ticker):
    try:
        return str(round(si.get_live_price(ticker),2))
    except:
        return ('Not a valid ticker.')

def return_current_prices(tickers):
    prices = {}
    for ticker in tickers:
        prices[ticker]=return_current_price(ticker)
    return prices