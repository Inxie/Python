from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secretKey1'

@app.route("/")
def renderCount():
    if 'number' not in session:
        session['number'] = 0
    else:
        session['number'] += 1
    return render_template("index.html")

@app.route("/destroy_session")
def deleteCount():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)