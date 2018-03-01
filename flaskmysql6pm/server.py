from flask import Flask, render_template, redirect, session, request, flash
app = Flask(__name__)
app.secret_key = "Mysecretkey"
from myconnection import MySQLConnector
mysql = MySQLConnector(app, "twitter6pm")

x = mysql.query_db("SELECT * FROM users")
print x

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    query = "INSERT INTO `twitter6pm`.`users` (`username`, `password`, `created_at`, `updated_at`) VALUES (:spot_one, :spot_two, now(), now());"
    data = {
        "spot_one":request.form["username"],
        "spot_two":request.form["password"]
    }
    mysql.query_db(query, data)
    flash("Successfully registered. Please login.")
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    query = "SELECT * FROM users WHERE username = :username"
    data = {
        "username":request.form["username"],
    }
    users = mysql.query_db(query, data)
    if len(users) > 0:
        user = users[0] #the first dictionary
        if user["password"] == request.form["password"]:
            session["id"] = user["id"]
            return "logged in"
        else:
            flash("wrong password")
            return redirect("/")
    else:
        flash("email doesnt exist")
        return redirect("/")
app.run(debug=True)