from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def read_all():
    return render_template("read_all.html")

@app.route("/create")
def insert_new():
    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)