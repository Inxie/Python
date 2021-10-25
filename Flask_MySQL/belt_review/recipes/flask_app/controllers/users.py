from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

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

@app.route("/recipes/new", methods=["POST","GET"])
def new_recipe():
    if request.method == "POST":
        if "user_id" not in session:
            return redirect("/logout")
        data = {
            "name": request.form["name"],
            "made_on": request.form["made_on"],
            "under_30": request.form["under_30"],
            "description": request.form["description"],
            "instructions": request.form["instructions"],
            "user_id": session.get("user_id")
        }
        Recipe.new_recipe(data)
        if Recipe.validate(request.form):
            return render_template("new.html")
        else:
            return redirect("/recipes/new")
    else:
        return render_template("new.html")

@app.route("/recipes/<int:id>")
def show_one_recipe(id):
    data = {
        "recipe_id":id
    }
    one_recipe = User.one_recipe(data)
    return render_template("recipes.html", one_recipe=one_recipe)