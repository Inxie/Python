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

@app.route("/user/<int:id>")
def show_one(id):
    data = {
        "id":id
    }
    user = Users.show_one(data)
    return render_template("one_user.html", user=user)

@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        "id":id
    }
    user = Users.show_one(data)
    return render_template("edit_user.html", user=user)

@app.route("/edituser/<int:id>", methods=["POST"])
def edit_user_db(id):
    print (request.form)
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id":id
    }
    Users.edit_user(data)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    Users.delete_user(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)