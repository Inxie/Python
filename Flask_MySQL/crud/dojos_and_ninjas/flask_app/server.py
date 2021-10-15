from flask_app import app
from flask_app.controllers import dojoninjas
app = Flask(__name__)

@app.route("/")
def all_dojos():
    dojos = Dojos.all_dojos()
    return render_template("dojos.html", dojos=dojos)