from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'My super secret app' # you need to set a secret key for security purposes

@app.route('/')
def index():
  return render_template("index.html")

app.run(debug=True)