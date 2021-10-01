from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<nums>")
def checkerBoard(nums):
    repeat = int(nums)//2
    return render_template('index2.html', repeat=repeat)

@app.route("/<x>/<y>")
def bothChecker(x,y):
    repeat1 = int(x)//2
    repeat2 = int(y)//2
    return render_template('index3.html', repeat1=repeat1, repeat2=repeat2)

if __name__=="__main__":
    app.run(debug=True)