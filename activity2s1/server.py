from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process_data():
    print request.form
    name = request.form['name']
    gender = request.form['gender']
    location = request.form['location']
    return render_template('results.html', name=name, gender=gender, location=location)
@app.route('/hobbies')
def show_hobbies():
    return render_template('hobbies.html', hobbies=["sports", "cooking", "coding", "reading"])
app.run(debug=True)