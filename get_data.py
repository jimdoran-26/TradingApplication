from yahoo_fin import stock_info as si
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

#helpers
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
        return str(si.get_live_price(ticker))
    except:
        return ('Not a valid ticker.')

def return_current_prices(tickers):
    prices = {}
    for ticker in tickers:
        prices[ticker]=return_current_price(ticker)
    return prices

#GET A CHART OF A STOCK/STOCKS PRICES WITH AN INPUTTED TIME FRAME
def chart_of_stock(ticker,start_date,end_date):
    stock = price_grab(ticker,start_date,end_date)

    #create chart
    plt.figure(figsize=(10, 6))
    plt.title(start_date+' to ' + end_date +' ' + ticker+' adjusted close price')
    plt.ylabel("price in USD")
    plt.xlabel('date')

    plt.plot(stock[ticker])
    plt.show()

def chart_of_stocks(tickers,start_date,end_date):
    #create chart
    plt.figure(figsize=(10, 6))
    plt.title(start_date + ' to ' + end_date + ' '  + 'adjusted close price')
    plt.ylabel("price in USD")
    plt.xlabel('date')

    stock = price_grab(tickers,start_date,end_date)

    for ticker in tickers:
        plt.plot(stock[ticker],label=ticker)

    plt.legend(loc="upper left")
    plt.show()

#GET CHART OF STOCK/STOCKS RETURNS WITH INPUTTED TIME FRAME
def chart_of_stock_returns(ticker,start_date,end_date):
    cum_return=returns_grab(ticker,start_date,end_date)

    # create chart
    plt.figure(figsize=(10, 6))
    plt.title(start_date + ' to ' + end_date + ' ' + ticker + ' returns')
    plt.ylabel("% returns")
    plt.xlabel('date')

    plt.plot(cum_return[ticker])
    plt.show()


def chart_of_stocks_returns(tickers,start_date,end_date):
    cum_returns = returns_grab(tickers, start_date, end_date)

    # create chart
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