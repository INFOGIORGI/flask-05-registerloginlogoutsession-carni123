from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="138.41.20.102"
app.config['MYSQL_PORT']=53306
app.config['MYSQL_USER']="ospite"
app.config['MYSQL_PASSWORD']="ospite"
app.config['MYSQL_DB']="w3schools"

mysql=MySQL(app)

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