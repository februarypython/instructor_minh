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

            query = "SELECT tweets AS content, DATE_FORMAT(created_at, '%m/%d/%y')AS tweet_date FROM tweets WHERE tweets.users_id="+str(session['id'])
            results = mysql.query_db(query)
            return render_template('dashboard.html', all_tweets=results) # pass data to our template
        else:
            flash("wrong password")
            return redirect("/")
    else:
        flash("email doesnt exist")
        return redirect("/")

@app.route("/addtweet", methods=["POST"])
def addtweet():
    # Write users info query as a string. 
    query = "INSERT INTO tweets ( tweets, users_id, created_at, updated_at) VALUES (:content, :loggedin_id, NOW(), NOW() )"
    # We'll then create a dictionary of data from the POST data received.
    data = {
            'content': request.form['content'],
            'loggedin_id': session['id']
            }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    # run query to get all of users.id tweets
    query = "SELECT tweets AS content, DATE_FORMAT(created_at, '%m/%d/%y')AS tweet_date FROM tweets WHERE tweets.users_id="+str(session['id'])
    results = mysql.query_db(query)

    return render_template('dashboard.html', all_tweets=results) # pass data to our template

app.run(debug=True)