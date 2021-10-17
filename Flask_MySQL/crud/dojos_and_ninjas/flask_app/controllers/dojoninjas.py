from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.ninja import Ninjas
from flask_app.models.dojo import Dojos

@app.route("/")
def all_dojos():
    dojos = Dojos.all_dojos()
    return render_template("dojos.html", dojos=dojos)

@app.route("/newdojo", methods=["POST", "GET"])
def new_dojo():
    if request.method == "POST":
        data = {
                "name": request.form["name"]
            }
        Dojos.new_dojo(data)
        return redirect("/")
    else:
        return render_template("dojos.html")

@app.route("/newninja", methods=["POST", "GET"])
def new_ninja():
    if request.method == "POST":
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "age": request.form["age"],
            "dojo_id": request.form["dojo_id"]
        }
        Ninjas.new_ninja(data)
        return redirect("/")
    else:
        return render_template("new_ninja.html")

@app.route("/dojo/<int:id>")
def show_one_dojo(id):
    data = {
        "id":id
    }
    dojos_ninjas = Dojos.one_dojos_ninjas(data)
    return render_template("one_dojo.html", dojos_ninjas=dojos_ninjas)