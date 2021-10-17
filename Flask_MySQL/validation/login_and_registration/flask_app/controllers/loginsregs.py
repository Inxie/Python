from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.models.loginreg import Register

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route('/register', methods=["POST"])
def new_user():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password" : pw_hash,
        "confirm_password": pw_hash
    }
    
    new_user_id = Register.save_registration(data)
    session["new_user_id"] = new_user_id
    
    if Register.validate_registration(request.form):
        return render_template("registered.html")
    else:
        return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_is_registered = Register.check_by_email(data)
    # user is not registered in the db
    if not user_is_registered:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_is_registered.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_is_registered.id
    # never render on a post!!!
    return render_template("registered.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")