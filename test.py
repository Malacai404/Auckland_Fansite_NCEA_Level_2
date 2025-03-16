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
@app.route('/team')
def team():
    return render_template("team.html")
@app.route('/club')
def club():
    return render_template("club.html")
@app.route('/sponsorships')
def sponsorships():
    return render_template("sponsorships.html")
@app.route('/top_ten')
def top_ten():
    return render_template("top_ten.html")
@app.route('/a_league_table')
def a_league_table():
    return render_template("a_league_table.html")

if __name__ == "__main__":
    app.run(debug=True)