from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'yoyothingsstartgettingharder'

@app.route('/')
def index():
    if 'users' in session:
        print session['users']
    if 'email' in session:
        return redirect('/home')
    return render_template('index.html')

@app.route('/process_form/<action>', methods=['post'])
def process(action):
    if 'users' not in session:
        session['users'] = []
    if action == 'register':
        for user in session['users']:
            if user['email'] == request.form['email']:
                flash('email already exits')
                return redirect('/')
        session['users'].append(request.form)
        flash('Thanks for registering, please log in')
        return redirect('/')
    elif action == 'login':
        for user in session['users']:
            if user['email'] == request.form['email'] and user['password'] == request.form['password']:
                session['email'] = user['email']
                return redirect('/home')
        flash('Wrong email password combination')
        return redirect('/')
    else:
        return redirect('/')
@app.route('/home')
def home():
    for user in session['users']:
        if user['email'] == session['email']:
            return render_template('home.html', logged_user=user)

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')
app.run(debug=True)
