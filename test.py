from flask import Flask, render_template, g
import sqlite3
app = Flask(__name__)
DATABASE = 'static/database.db'

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    sql = "SELECT players.player_photo_url, players.player_name FROM players;"
    results = query_db(sql)
    names_urls = []
    for l in results:
        names_urls.extend(l)
    return render_template("index.html", names_urls=names_urls)
@app.route('/admin')
def admin():
    return "<h1>Hello Admin!</h1>"

if __name__ == "__main__":
    app.run(debug=True)