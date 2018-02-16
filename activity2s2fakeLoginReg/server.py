from flask import Flask, render_template, redirect, session, request, flash
app = Flask(__name__)
app.secret_key = 'My super secret app' # you need to set a secret key for security purposes

@app.route('/') #
def index():
  #print users just to see
  if "users" in session:
    print session["users"]
  if "email" in session:
    return redirect("/home")
  return render_template("index.html")


@app.route("/process_form/<action>", methods=["POST"])
def process(action):
  if "users" not in session:
    session["users"] = []
  if action == "register":
    #check for user
    for user in session["users"]:
      if user["email"] == request.form["email"]:
        flash("email already exist")
        return redirect("/")
    #if we reach this point, for loop finished without user["email"] == request.form["email"], we can register
    session["users"].append(request.form)
    flash("Thanks for registering, please login")
    return redirect("/")
  elif action == "login":
    #for loop through each user in session and checks email and password. If match, set session["email"] and redirect to home
    for user in session["users"]:
      if user["email"] == request.form["email"] and user["password"] == request.form["password"]:
        session["email"] = user["email"]
        return redirect("/home")
    #flash a message and redirect to index
    flash("Wrong email password combination")
    return redirect("/")
  else:
    return redirect("/")

@app.route("/home")
def home():
  #find user in "database"
  for user in session["users"]:
    if user["email"] == session["email"]:
      return render_template("home.html", logged_user=user)

@app.route("/clear_session")
def clear_session():
  session.clear()
  return redirect("/")
app.run(debug=True)