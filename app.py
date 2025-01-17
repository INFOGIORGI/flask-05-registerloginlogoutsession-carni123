from flask import Flask, request,redirect
from flask import render_template
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash
app = Flask(__name__)

app.config['MYSQL_HOST']="138.41.20.102"
app.config['MYSQL_PORT']=53306
app.config['MYSQL_USER']="ospite"
app.config['MYSQL_PASSWORD']="ospite"
app.config['MYSQL_DB']="w3schools"

mysql=MySQL(app)
app.secret_key = 'your-secret-key-here'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register/",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
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
                cursor.execute(query_insert,(username,generate_password_hash(password),nome,cognome))
                mysql.connection.commit()
                return redirect("/")
            else:
                flash("username gia presente")
                return redirect("/register/")
        else:
            flash("password non coincidono")
            return redirect("/register/")


@app.route("/log_in/", methods=["GET","POST"])
def log_in():
    if request.method == "GET":
        return render_template("log_in.html")
    else:
        username=request.form.get("username")
        password=request.form.get("password")
        cursor=mysql.connection.cursor()
        query="""SELECT * FROM users WHERE username=%s """
        cursor.execute(query,(username,))
        data=cursor.fetchall()
        
        if len(data) == 0:
            return render_template("log_in.html", errore=username+" "+password)
        else:
            password_db=data[0][1]
            if check_password_hash(password_db,password):
                return redirect("/personale")
            else:
                return redirect("/log_in/")



        
@app.route("/personale")
def log_out():
    return render_template("personale.html")


app.run(debug=True)