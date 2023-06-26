import pygal
from flask import Flask, render_template, request, url_for, flash, redirect, abort
import csv
import requests

# make a Flask application object called app
app = Flask(__name__)
av_api_key = "WYJJIS12BT0A73WB"

app.config["DEBUG"] = True

# use the app.route() decorator to create a Flask view function called index(). This displayes when the site home age is requested 
@app.route('/', methods=('GET', 'POST'))
def index():
    tickers = []
    with open('stocks.csv') as stocks_file:
        csv_reader = csv.reader(stocks_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                tickers.append(row[0])
                line_count += 1


    if request.method == 'POST':
        stock_chosen = request.form['stock_ticker']
        chart_type = request.form['chart_type']
        time_series = request.form['time_series']
        if chart_type = "Bar":
            chart = pygal.Bar()
        else:
            chart = pygal.Line()
        
        if time_series == "Intraday":
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_chosen}&interval=15min&apikey='+av_api_key
            r = requests.get(url)
            data = r.json()
            stock_info = data["Time Series (15min)"]
        elif time_series == "Daily":
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock_chosen}&apikey='+av_api_key
            r = requests.get(url)
            data = r.json()
            stock_info = data["Time Series (Daily)"]
        elif time_series == "Weekly":
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock_chosen}&apikey='+av_api_key
            r = requests.get(url)
            data = r.json()
            stock_info = data["Time Series (Daily)"]
        elif time_series == "Monthly":
            pass

    if request.method == 'POSTs':
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GOOGL&interval=15min&apikey='+av_api_key
        r = requests.get(url)
        data = r.json()
        stock_info = data["Time Series (15min)"]
        time_info = []
        open_info = []
        counter = 0
        for key in stock_info:
            time_info.insert(0, key)
            open_info.insert(0, float(stock_info[key]['1. open']))
            counter += 1
            if counter == 11:
                break

        print(time_info)
        print(open_info)

        line_chart = pygal.Line()
        line_chart.title = 'GOOGL'
        line_chart.x_labels = time_info
        line_chart.add('Open', open_info)

        chart = line_chart.render_data_uri()


        """
        line_chart = pygal.Line()
        line_chart.title = 'Browser usage evolution (in %)'
        line_chart.x_labels = map(str, range(2002, 2013))
        line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
        line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
        line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
        chart = line_chart.render_data_uri()
        """

        return render_template("index.html", chart=chart, tickers=tickers)

    return render_template("index.html", tickers=tickers)

#run the flask
app.run(host="0.0.0.0")