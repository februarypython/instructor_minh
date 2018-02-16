from flask import Flask, render_template, redirect, session, request, flash
app = Flask(__name__)
app.secret_key = 'My super secret app' # you need to set a secret key for security purposes

@app.route('/') #
def index():
  if "users" in session:
    print session["users"]
  if "email" in session:
    return redirect("/home")
  return render_template("index.html")

@app.route("/process_info/<action>", methods=["POST"])
def process(action):
  if "users" not in session:
    session["users"] = []
  if action == "register":
    session["users"].append(request.form)
    flash("Thanks for registering, please login")
    return redirect("/")
  elif action == "login":
    for user in session["users"]:
      if user["email"] == request.form["email"] and user["password"] == request.form["password"]:
        session["email"] = user["email"]
        return redirect("/home")
  else:
    return redirect("/")

app.run(debug=True)