from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/') #our index.html page will handle rendering our form
def index():
    blogger_name="Cindy Kalkomey"
    blogger_photo="images/grp_sunset.jpg"
    return render_template('index.html', name=blogger_name, photo=blogger_photo)

@app.route('/process', methods=['POST'])  
def process():
    name = request.form["name"]
    location = request.form["location"]
    gender = request.form["gender"]    
    return render_template('process.html', name=name, location=location, gender=gender)

@app.route('/hobbies')
def hobbies():
    hobbies = ["Sports", "cooking", "coding"]
    return render_template('hobbies.html', hobbies=hobbies)

app.run(debug=True) 