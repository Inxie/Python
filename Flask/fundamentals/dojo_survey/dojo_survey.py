from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secretKey2'

@app.route("/")
def showFirst():
    return render_template("index.html")

@app.route('/result', methods=["GET",'POST'])
def create_user():
    if request.method == "POST":
        session['name'] = request.form['yourName']
        session['location'] = request.form['dojoLocation']
        session['language'] = request.form['favLanguage']
        session['comment'] = request.form['commentsOpt']
        return render_template("index2.html", name = request.form['yourName'], location = request.form['dojoLocation'], language = request.form['favLanguage'], comment = request.form['commentsOpt'])

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)