###################################################
######                                       ######
######            pyblog/routes.py           ###### 
######                                       ######
###################################################

from pyblog import app
import flask

@app.route('/')
@app.route('/home')
def homepage():
    return flask.render_template("home.jin")

@app.route('/contact')
def contact():
    return flask.render_template("contact.jin")
