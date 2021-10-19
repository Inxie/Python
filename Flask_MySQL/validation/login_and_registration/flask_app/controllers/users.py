from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register', methods=["POST"])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password" : pw_hash,
        "confirm_password": pw_hash
    }
    
    id = User.save(data)
    session["user_id"] = id
    return redirect("/dashboard")

@app.route('/login', methods=["POST"])
def login():
    data = { 
        "email": request.form["email"] 
    }

    user_is_registered = User.check_by_email(data)

    if not user_is_registered:
        flash("Invalid Email.")
        return redirect("/")
    if not bcrypt.check_password_hash(user_is_registered.password, request.form['password']):

        flash("Invalid Password.")
        return redirect('/')

    session["user_id"] = user_is_registered.id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id": session["user_id"]
    }
    return render_template("dashboard.html", user=User.check_by_id(data))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")