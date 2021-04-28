from get_data import *

def chart_of_stock(ticker,start_date,end_date):#todo exception handling
    stock = price_grab(ticker,start_date,end_date)
    #create chart
    plt.figure(figsize=(10, 6))
    plt.title(start_date+' to ' + end_date +' ' + ticker+' adjusted close price')
    plt.ylabel("price in USD")
    plt.xlabel('date')

    plt.plot(stock[ticker])
    # plt.show()
    test = 'Static/chart_of_price.png'
    plt.savefig(test)

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
    # plt.show()
    test = 'Static/chart_of_prices.png'
    plt.savefig(test)