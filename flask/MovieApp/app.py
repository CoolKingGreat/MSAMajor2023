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
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        if request.form['action'] == 'title_search':
            conn = get_db_connection()
            posts = conn.execute('SELECT * FROM "movies" WHERE title LIKE :search ORDER BY imdb_score DESC', {"search": '%' + request.form['search_text'] + '%'}).fetchall()
            conn.close() 
            return render_template('index.html', posts=posts)
        elif request.form['action'] == 'director_search':
            conn = get_db_connection()
            posts = conn.execute('SELECT * FROM "movies" WHERE director LIKE :search ORDER BY imdb_score DESC', {"search": '%' + request.form['search_text'] + '%'}).fetchall()
            conn.close() 
            return render_template('index.html', posts=posts)
        elif request.form['action'] == 'rating_search':
            conn = get_db_connection()
            posts = conn.execute('SELECT * FROM "movies" WHERE rating LIKE :search ORDER BY imdb_score DESC', {"search": request.form['search_text'] + '%'}).fetchall()
            conn.close() 
            return render_template('index.html', posts=posts)
        elif request.form['action'] == 'genre_search':
            conn = get_db_connection()
            posts = conn.execute('SELECT * FROM "movies" WHERE genres LIKE :search ORDER BY imdb_score DESC', {"search": "%" + request.form['search_text'] + '%'}).fetchall()
            conn.close() 
            return render_template('index.html', posts=posts)
        
        elif request.form['action'] == 'year_sort':
            conn = get_db_connection()
            posts = conn.execute('SELECT * FROM "movies" ORDER BY year DESC').fetchall()
            conn.close() 
            return render_template('index.html', posts=posts)
        
        elif request.form['action'] == 'runtime_sort':
            conn = get_db_connection()
            posts = conn.execute('SELECT * FROM "movies" ORDER BY runtime DESC').fetchall()
            conn.close() 
            return render_template('index.html', posts=posts)
        
        elif request.form['action'] == 'imdb_sort':
            conn = get_db_connection()
            posts = conn.execute('SELECT * FROM "movies" ORDER BY imdb_score DESC').fetchall()
            conn.close() 
            return render_template('index.html', posts=posts)
        
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM "movies" ORDER BY imdb_score DESC').fetchall()
    conn.close() 
    #send the posts to the index.html template to be displayed
    return render_template('index.html', posts=posts)

@app.route('/actors', methods=('GET', 'POST'))
def actors():

    conn = get_db_connection()
    posts = conn.execute('SELECT actors.name, movies.title FROM actors, movies WHERE actors.movie_id = movies.id').fetchall()
    actor_info = {}
    for post in posts:
        if post['name'] not in actor_info.keys():
            actor_info[post['name']] = post['title']
        else:
            actor_info[post['name']] += ", "+post['title']
    conn.close() 
    #send the posts to the index.html template to be displayed
    return render_template('actors.html', actor_info=actor_info, posts=posts)

@app.route('/director/<name>/', methods=('GET', 'POST'))
def director(name):
    if request.method == "POST":
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM "movies" WHERE director=? ORDER BY imdb_score DESC', (name, )).fetchall()
    conn.close() 
    return render_template('director.html', name=name, posts=posts)

@app.route('/movie/<int:id>/', methods=('GET', 'POST'))
def movie(id):
    if request.method == "POST":
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    movie = conn.execute('SELECT * FROM "movies" WHERE id=? ORDER BY imdb_score DESC', (id, )).fetchone()
    conn.close() 
    return render_template('movie.html', movie=movie)

@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    #get post id
    conn = get_db_connection()
    conn.execute('DELETE FROM movies WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    #redirect to the index page
    return redirect(url_for('index'))


#run the flask
app.run(host="0.0.0.0")