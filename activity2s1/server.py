from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name="Alex")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["myName"]
    location = request.form["location"]
    gender = request.form["gender"]
    return render_template("formdata.html", name=name, location=location, gender=gender)

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html", hobbies = ["Coding", "Reading", "Traveling"])
app.run(debug=True)
