import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

# make a Flask application object called app
app = Flask(__name__)

app.config["DEBUG"] = True

# flash uses the secret key to secure sessions that remember information from one request to another
# This is for the error messages
app.config['SECRET_KEY'] = 'your secret key'


# Function to open a connection to the database.db file
def get_db_connection():
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    return conn

# use the app.route() decorator to create a Flask view function called index(). This displayes when the site home age is requested 
@app.route('/')
def index():

    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM movies').fetchall()
    conn.close() 

    print(posts)

    #send the posts to the index.html template to be displayed
    return render_template('index.html', posts=posts)

#run the flask
app.run(host="0.0.0.0")