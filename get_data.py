from yahoo_fin import stock_info as si
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

#GET THE CURRENT PRICE OF STOCK/STOCKS
def return_current_price(ticker):
    try:
        return si.get_live_price(ticker)
    except:
        return ('Not a valid ticker.')

def return_current_prices(tickers):
    prices = {}
    for ticker in tickers:
        prices[ticker]=return_current_price(ticker)
    return prices

#GET A CHART OF A STOCK/STOCKS PRICES WITH AN INPUTTED TIME FRAME
def chart_of_stock(ticker,start_date,end_date):
    #create chart
    stock = pd.DataFrame()
    stock[ticker] = wb.DataReader(ticker, data_source='yahoo', start=start_date, end=end_date)['Adj Close']
    plt.figure(figsize=(10, 6))
    plt.title(start_date+' to ' + end_date +' ' + ticker+' adjusted close price')
    plt.ylabel("price in USD")
    plt.xlabel('date')

    plt.plot(stock[ticker])
    plt.show()

def chart_of_stocks(tickers,start_date,end_date):
    #create chart
    stock = pd.DataFrame()
    plt.figure(figsize=(10, 6))
    plt.title(start_date + ' to ' + end_date + ' '  + 'adjusted close price')
    plt.ylabel("price in USD")
    plt.xlabel('date')

    for ticker in tickers:
        stock[ticker] = wb.DataReader(ticker, data_source='yahoo', start=start_date, end=end_date)['Adj Close']
        plt.plot(stock[ticker],label=ticker)
    plt.legend(loc="upper left")
    plt.show()

#GET CHART OF STOCK/STOCKS RETURNS WITH INPUTTED TIME FRAME
def chart_of_stocks_returns(tickers,start_date,end_date):
    #stock price grab
    prices = pd.DataFrame()
    returns = pd.DataFrame()
    for ticker in tickers:
        prices[ticker] = wb.DataReader(ticker, data_source='yahoo', start=start_date, end=end_date)['Adj Close']

    #calculate returns
    for ticker in prices:
        returns[ticker] = (prices[ticker] / prices[ticker].shift(1)) - 1

    #cumulative returns
    cum_returns = pd.DataFrame()
    for ticker in returns:
        cum_returns[ticker] = 100 * (np.exp(np.log1p(returns[ticker]).cumsum()) - 1)

    # create chart
    stock = pd.DataFrame()
    plt.figure(figsize=(10, 6))
    plt.title(start_date + ' to ' + end_date + ' ' + 'returns')
    plt.ylabel("% returns")
    plt.xlabel('date')

    #graph returns
    j=0
    for i in cum_returns:
        plt.plot(cum_returns[i],label=i)
        j+=1
    plt.legend(loc="upper left")
    plt.show()



