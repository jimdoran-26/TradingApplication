from get_data import *


#GET CHART OF STOCK/STOCKS RETURNS WITH INPUTTED TIME FRAME
def chart_of_stock_returns(ticker,start_date,end_date):
    cum_return=returns_grab(ticker,start_date,end_date)

    # create chart
    plt.figure(figsize=(10, 6))
    plt.title(start_date + ' to ' + end_date + ' ' + ticker + ' returns')
    plt.ylabel("% returns")
    plt.xlabel('date')

    plt.plot(cum_return[ticker])
    #plt.show()
    test = 'Static/chart_of_stock_returns.png'
    plt.savefig(test)


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
    # plt.show()
    test = 'Static/chart_of_stocks_returns.png'
    plt.savefig(test)