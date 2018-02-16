from flask import Flask, redirect, render_template, flash, session, request
app = Flask(__name__)
app.secret_key = "SAERKASDFKSJD"

# being table to take data in
# being able to display data out
@app.route("/")
def index():
    name = "Minh"
    if "quotes" not in session:
        session["quotes"] = []
    if "count" not in session:
        session["count"] = 1
    return render_template("index.html", display_name=name)

@app.route("/process_form", methods=["POST"])
def process_form():
    if "quotes" not in session:
        session["quotes"] = []
    quote = {
        "content":request.form["content"], "posted_by":request.form["posted_by"],
        "id":session["count"]
    }
    session["count"] += 1
    session["quotes"].append(quote)
    return redirect("/display_quotes")

@app.route("/display_quotes")
def display_quotes():
    print session["quotes"]
    return render_template("display_quote.html", quotes=session["quotes"])

@app.route("/display/<tweet_id>")
def display(tweet_id):
    for quote in session["quotes"]:
        if quote["id"] == int(tweet_id):
            display_quote = quote
    
    return render_template("display.html", quote=display_quote)

@app.route("/clear_session")
def clear():
    session.clear()
    return redirect("/")
app.run(debug=True)