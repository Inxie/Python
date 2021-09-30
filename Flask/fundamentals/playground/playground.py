from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def index():
    return render_template('index.html')

@app.route("/play/<boxNums>")
def blueBoxes_repeat(boxNums):
    repeat = int(boxNums)
    return render_template('index2.html', repeat=repeat)
    
@app.route("/play/<boxNums>/<colorNew>")
def colorBoxes(boxNums, colorNew):
    repeat = int(boxNums)
    return render_template('index3.html', repeat=repeat, colorNew=colorNew)

if __name__=="__main__":
    app.run(debug=True)