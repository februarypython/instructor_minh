from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'Secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def usercreation():
    name = request.form['name']
    gender = request.form['gender']
    location = request.form['location']
    return render_template('process.html', name1 = name, gender1 = gender, location1 = location)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

app.run(debug=True)