#################################################
#######                                   #######
#######             __INIT__.PY           #######
#######                                   ####### 
#################################################

import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'reuvenkey'
from pyblog import routes
