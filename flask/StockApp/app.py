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
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        prev_info = [stock_chosen, chart_type, time_series, start_date, end_date]

        if not (stock_chosen or chart_type or time_series or start_date or end_date):
            return render_template("index.html", tickers=tickers, alert="Enter all values")

        if chart_type == "Bar":
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
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={stock_chosen}&apikey='+av_api_key
            r = requests.get(url)
            data = r.json()
            stock_info = data["Weekly Time Series"]
        elif time_series == "Monthly":
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={stock_chosen}&apikey='+av_api_key
            r = requests.get(url)
            data = r.json()
            stock_info = data["Monthly Time Series"]
        
        time_info = []
        open_info = []
        high_info = []
        low_info = []
        close_info = []
        
        for key in stock_info:
            time_info.insert(0, key)
            open_info.insert(0, float(stock_info[key]['1. open']))
            high_info.insert(0, float(stock_info[key]['2. high']))
            low_info.insert(0, float(stock_info[key]['3. low']))
            close_info.insert(0, float(stock_info[key]['4. close']))


        if (time_series == "Intraday" and (start_date<time_info[0].split()[0] or start_date>time_info[-1].split()[0] or end_date<time_info[0].split()[0]  or end_date>time_info[-1].split()[0])) or (time_series != "Intraday" and (start_date<time_info[0] or start_date>time_info[-1] or end_date<time_info[0] or end_date>time_info[-1])) or start_date > end_date:
            return render_template("index.html", tickers=tickers, alert="Invalid Date / Not in Range")

        actual_info = [[],[],[],[],[]]
        counter = 0
        if time_series != "Intraday":
            while counter < len(time_info):
                if time_info[counter] >= start_date and time_info[counter] <= end_date:
                    actual_info[0].append(time_info[counter])
                    actual_info[1].append(open_info[counter])
                    actual_info[2].append(high_info[counter])
                    actual_info[3].append(low_info[counter])
                    actual_info[4].append(close_info[counter])
                counter += 1
            
            time_info = actual_info[0]
            open_info = actual_info[1]
            high_info = actual_info[2]
            low_info = actual_info[3]
            close_info = actual_info[4]
        else:
            while counter < len(time_info):
                if time_info[counter].split()[0] >= start_date and time_info[counter].split()[0] <= end_date:
                    actual_info[0].append(time_info[counter])
                    actual_info[1].append(open_info[counter])
                    actual_info[2].append(high_info[counter])
                    actual_info[3].append(low_info[counter])
                    actual_info[4].append(close_info[counter])
                counter += 1
            

            time_info = actual_info[0]
            open_info = actual_info[1]
            high_info = actual_info[2]
            low_info = actual_info[3]
            close_info = actual_info[4]
        

        chart.title = stock_chosen
        chart.x_labels = time_info
        chart.add('Open', open_info)
        chart.add('High', high_info)
        chart.add('Low', low_info)
        chart.add('Close', close_info)

        chart = chart.render_data_uri()
        return render_template("index.html", chart=chart, tickers=tickers)

    return render_template("index.html", tickers=tickers)

#run the flask
app.run(host="0.0.0.0")