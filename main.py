from get_data import *
from actions.returns import *
from actions.prices import *

def main():
    print(return_current_price('aapl'))
    print(return_current_prices(['aapl','penn','msft']))
    print(chart_of_stock('aapl','2006-10-02','2011-12-30'))
    print(chart_of_stocks(['aapl','penn','msft'],'2006-10-02','2011-12-30'))
    print(chart_of_stock_returns('aapl','2020-01-01','2021-01-01'))
    print(chart_of_stocks_returns(['aapl','penn','msft'],'2020-01-01','2021-01-01'))

if __name__ == "__main__":
    main()