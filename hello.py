from get_data import *
from flask import Flask, render_template, request, redirect, url_for
import matplotlib
from actions.returns import *
from actions.prices import *

matplotlib.use('Agg')

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello():
    return render_template('hello.html')

# @app.route('/return_current_price')
# def current_price():
#     price= return_current_price('aapl')
#     return render_template('current_price.html',value='aapl',value2=price)

@app.route('/get_ticker')
def get_ticker():
    return render_template('temp.html')

@app.route('/get_ticker', methods=['POST'])
def get_ticker_post():
    text = request.form['text']
    processed_text = text.upper()
    price = return_current_price(processed_text)
    return render_template('current_price.html', value=processed_text, value2=price)


@app.route('/price_chart')
def get_ticker_dates():
    return render_template('get_ticker_dates.html')

@app.route('/price_chart',methods=['POST'])
def price_chart():
    text = request.form['text']
    start_date = request.form['start']
    end_date = request.form['end']

    processed_text = text.upper()
    chart_of_stock(processed_text,start_date,end_date)

    return render_template('stock_price_chart.html',value=processed_text)


@app.route('/prices_chart')#todo
def prices_chart():
    chart_of_stocks(['aapl','penn','msft'],'2020-01-01','2021-01-01')
    return render_template('stock_prices_chart.html')


@app.route('/return_chart')
def get_ticker_dates_return():
    return render_template('get_ticker_dates.html')

@app.route('/return_chart',methods=['POST'])
def return_chart():
    text = request.form['text']
    start_date = request.form['start']
    end_date = request.form['end']

    processed_text = text.upper()
    chart_of_stock_returns(processed_text, start_date, end_date)

    return render_template('stock_returns_chart.html', value=processed_text)

@app.route('/returns_chart')#todo
def returns_chart():
    chart_of_stocks_returns(['aapl','penn','msft'],'2020-01-01','2021-01-01')
    return render_template('stocks_returns_chart.html')

