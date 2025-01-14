from flask import Flask, request,redirect
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

@app.route("/register/",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html",titolo="Register")
    else:
        cursor=mysql.connection.cursor()
        query_select="""SELECT username from users where username=%s"""
        nome=request.form.get("nome")
        cognome=request.form.get("cognome")
        username=request.form.get("username")
        password=request.form.get("password")
        confpassword=request.form.get("confirmpassword")
        
        if password==confpassword:
            cursor.execute(query_select,(username,))
            usr=cursor.fetchall()
            if len(usr)==0:
                query_insert="""INSERT into users VALUES(%s,%s,%s,%s )"""
                cursor.execute(query_insert,(username,password,nome,cognome))
                #cursor.fetchall()
                mysql.connection.commit()
                return redirect("/")
            else:
                return render_template("register.html", titolo="errore")


@app.route("/log_in")
def log_in():
    return render_template("log_in.html",titolo="Log in")

@app.route("/personale")
def log_out():
    return render_template("personale.html",titolo="Personale")


app.run(debug=True)