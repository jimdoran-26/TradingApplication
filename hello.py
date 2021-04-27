from get_data import *
from flask import Flask, render_template
import matplotlib
from actions.returns import *
from actions.prices import *

matplotlib.use('Agg')

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/return_current_price')
def current_price():
    return return_current_price('aapl')

@app.route('/price_chart')
def price_chart():
    chart_of_stock('aapl','2020-01-01','2021-01-01')
    return render_template('stock_price_chart.html')

@app.route('/prices_chart')
def prices_chart():
    chart_of_stocks(['aapl','penn','msft'],'2020-01-01','2021-01-01')
    return render_template('stock_prices_chart.html')

@app.route('/return_chart')
def return_chart():
    chart_of_stock_returns('aapl','2020-01-01','2021-01-01')
    return render_template('stock_returns_chart.html')

@app.route('/returns_chart')
def returns_chart():
    chart_of_stocks_returns(['aapl','penn','msft'],'2020-01-01','2021-01-01')
    return render_template('stocks_returns_chart.html')