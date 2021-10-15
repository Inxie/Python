from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.dojoninja import Dojos
from flask_app.models.dojoninja import Ninjas



@app.route("/")
def all_dojos():
    dojos = Dojos.all_dojos()
    return render_template("dojos.html", dojos=dojos)