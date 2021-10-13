from flask import Flask, render_template, request, redirect, session
from user import Users
app = Flask(__name__)

@app.route("/")
def read_all():
    users = Users.read_all()
    return render_template("read_all.html", users=users)

# A way to combine methods below:
#
# @app.route("/create", methods=["POST", "GET"])
# def insert_new():
#     if request.method == "POST":
#         data = {
#             "first_name": request.form["first_name"],
#             "last_name": request.form["last_name"],
#             "email": request.form["email"]
#         }
#         Users.insert_new(data)
#         return redirect("/")
#     else:
#         return render_template("create.html")

@app.route("/create")
def createForm():
    return render_template("create.html")

@app.route("/createnew", methods=["POST"])
def insert_new():
    data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"]
        }
    Users.insert_new(data)
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)