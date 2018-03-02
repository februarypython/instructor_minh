from flask import Flask, render_template, redirect, session, request, flash
app = Flask(__name__)
app.secret_key = "Mysecretkey"
from myconnection import MySQLConnector
mysql = MySQLConnector(app, "twitter6pm")

@app.route("/")
def index():
    if "id" in session:
        return redirect("/dashboard")
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
            return redirect("/dashboard")
        else:
            flash("wrong password")
            return redirect("/")
    else:
        flash("email doesnt exist")
        return redirect("/")

@app.route("/dashboard")
def dashboard():
    if "id" not in session:
        return redirect("/")
    # GRAB ALL TWEETS
    query = "SELECT users_id, username,  tweets AS content, DATE_FORMAT(tweets.created_at, '%m/%d/%y')AS tweet_date FROM tweets JOIN users ON users_id = users.id"
    results = mysql.query_db(query)
    #GRAB ALL USERS
    user_query = "SELECT * FROM users"
    all_users = mysql.query_db(user_query)
    print all_users
    #GRAB ALL FOLLOWERS
    followers_query = "SELECT * FROM followers WHERE follower_id = :user_id"
    data = {
        "user_id":session["id"]
    }
    followings = mysql.query_db(followers_query, data)
    print followings
    list_of_leader_ids = []
    for following in followings:
        list_of_leader_ids.append(following["leader_id"])
    #gives just a list of ids that i am following so I can do a "if in" check
    print list_of_leader_ids
    return render_template('dashboard.html', all_tweets=results, users=all_users, leader_ids=list_of_leader_ids) # pass data to our template

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
    return redirect("/dashboard")
@app.route("/follow/<user_id>")
def follow(user_id):
    query = "INSERT INTO followers ( follower_id, leader_id) VALUES (:follower, :leader)"
    # We'll then create a dictionary of data from the POST data received.
    data = {
            'follower':session["id"],
            'leader':user_id
    }
    mysql.query_db(query, data)
    return redirect("/dashboard")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
app.run(debug=True)