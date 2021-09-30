from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'

@app.route("/dojo")
def dojo():
    return 'Dojo!'

@app.route("/say/<name>")
def hi(name):
    print(name)
    return "Hi " + name.capitalize() + "!"

@app.route("/repeat/<int>")
def repeating(int):
    if int == "35":
        print(int)
        return ("hello" * 35)
    if int == "80":
        print(int)
        return("bye" * 80)
    if int == "99":
        print(int)
        return("dogs" * 99)

if __name__=="__main__":
    app.run(debug=True)