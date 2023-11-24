from api.bm.views import bm_views
from flask import Flask, render_template
from flask_cors import CORS
from models import session
from models import *

app = Flask(__name__)
app.register_blueprint(bm_views)
cors = CORS(app, resources={r"/api/bm/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    session.close()


reports = []


@app.route('/', strict_slashes=False)
def homeroute():
    return render_template("index.html", reports=reports)


@app.route('/reports.html')
def reports():
    return render_template('reports.html')


@app.route('/budgeting.html')
def budgeting():
    return render_template('budgeting.html')


@app.route('/transaction.html')
def transaction():
    return render_template('transaction.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
