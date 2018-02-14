from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name="Gerso", students=["gerso", "jamies", "pietro"])

@app.route("/send_data", methods=["POST"])
def process_data():
    return request.form["first_name"]
app.run(debug=True)