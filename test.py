from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    name = "Shay"
    return render_template("index.html", name=name)
@app.route('/admin')
def admin():
    return "<h1>Hello Admin!</h1>"

if __name__ == "__main__":
    app.run(debug=True)