from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html",titolo="Register")

@app.route("/register")
def register():
    return render_template("register.html",titolo="Register")

@app.route("/log_in")
def log_in():
    return render_template("log_in.html",titolo="Log in")

@app.route("/personale")
def log_out():
    return render_template("personale.html",titolo="Personale")


app.run(debug=True)