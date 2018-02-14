from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name="Minh")

@app.route("/process", methods=["POST"])
def process():
    gender = request.form["gender"]
    name = request.form["first_name"]
    location = request.form["location"]
    return render_template("formdata.html", name=name, gender=gender, location=location)

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html", hobbies = ["Sports", "cooking", "coding"])
app.run(debug=True)