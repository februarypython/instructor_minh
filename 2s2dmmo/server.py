from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "asdfashdfjklahe"

@app.route("/")
def index():
    if "tweets" not in session:
        session["users"] = []
    if "count" not in session:
        session["count"] = 1
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if "tweets" not in session:
        session["tweets"] = []
    tweet = {
        "id":session["count"],
        "content":request.form["content"],
        "posted_by":request.form["posted_by"]
    }
    session["count"] = session["count"] + 1
    session["tweets"].append(tweet)
    print session["tweets"]
    return redirect("/display_tweets")

@app.route("/display_tweet/<tweet_id>")
def display(tweet_id):
    for tweet in session["tweets"]:
        if tweet["id"] == int(tweet_id):
            return str(tweet)
    

@app.route("/display_tweets")
def display_tweets():
    return render_template("display_tweets.html", tweets=session["tweets"])


app.run(debug=True)