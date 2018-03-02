from myconnection import MySQLConnector
from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "hello this is my session key"
mysql = MySQLConnector(app, "twitter4pm")
print "="*100
print mysql.query_db("SELECT * FROM users")
print "="*100

@app.route("/")
def index():
    if "logged_id" in session:
        return redirect ("/dashboard")
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    query = "INSERT INTO users (username, password, created_at, updated_at) VALUES (:username, :password, NOW(), NOW())"
    data = {
        "username":request.form["username"],
        "password":request.form["password"]
    }
    mysql.query_db(query, data)
    flash("Successfully registered")
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    query = "SELECT * FROM users WHERE username = :user_name"
    data = {
        "user_name":request.form["username"]
    }
    users = mysql.query_db(query, data) # [], [{}], [{},{},{}]
    if len(users) > 0:
        user = users[0]
        if user["password"] == request.form["password"]:
            session["logged_id"] = user["id"]
            return redirect("/dashboard")
        else:
            flash("password doesnt match")
            return redirect("/")
    else:
        flash("no username found")
        return redirect("/")

@app.route("/dashboard")
def dashbaord():
    if "logged_id" not in session:
        return redirect ("/")
    #GRABS USER LOGGED IN
    query1 = "SELECT * FROM users WHERE id = :user_id"
    data = {
        "user_id":session["logged_id"]
    }
    user = mysql.query_db(query1, data)
    #GRABS ALL USERS
    query2 = "SELECT * FROM users"
    users = mysql.query_db(query2)

    #GRAB ALL TWEETS BY USER
    query = "SELECT * FROM tweets"
    tweets = mysql.query_db(query)

    #GRAB LOGGED USERS FOLLOWINGS
    query = "SELECT leader FROM followers WHERE follower = :user_id"
    followings = mysql.query_db(query, data)
    print followings
    users_not_following = []
    for i in range(len(users)):
        flag = False
        for follow in followings:
            if follow["leader"] == users[i]["id"]:
                flag = True
        if flag == False:
            users_not_following.append(users[i])
        

    return render_template("dashboard.html", user=user[0], tweets=tweets, users=users_not_following, following_ids=followings)

@app.route("/tweet/create", methods=["POST"])
def tweet_create():
    if "logged_id" not in session:
        return redirect ("/")
    query = "INSERT INTO tweets (tweet, users_id, created_at, updated_at, likes) VALUES (:tweet, :users_id, NOW(), NOW(), 0)"
    data = {
        "tweet":request.form["tweet"],
        "users_id":session["logged_id"]
    }
    mysql.query_db(query, data)
    return redirect("/dashboard")
@app.route("/like/<tweet_id>")
def like_tweet(tweet_id):
    if "logged_id" not in session:
        return redirect ("/")
    query = "SELECT * FROM tweets WHERE id = :tweet"
    data = {
        "tweet":tweet_id,
    }
    tweet = mysql.query_db(query, data)
    query = "UPDATE `twitter4pm`.`tweets` SET `likes`=:likes WHERE `id`=:tweet;"
    data = {
        "tweet":tweet_id,
        "likes":tweet[0]["likes"]+1
    }
    mysql.query_db(query, data)
    return redirect("/dashboard")
@app.route("/follow/<leader_id>")
def follow(leader_id):
    if "logged_id" not in session:
        return redirect ("/")
    query = "INSERT INTO `followers` (`follower`, `leader`) VALUES (:follow_id, :leader_id);"
    data = {
        "follow_id":session["logged_id"],
        "leader_id":leader_id
    }
    mysql.query_db(query, data)
    return redirect("/dashboard")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
app.run(debug=True)
