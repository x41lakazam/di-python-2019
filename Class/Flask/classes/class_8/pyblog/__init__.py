#################################################
#######                                   #######
#######             __INIT__.PY           #######
#######                                   ####### 
#################################################

import flask
import flask_sqlalchemy
import flask_migrate
import os

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'reuvenkey'

# Define the path of the database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ os.path.join(os.path.dirname(__file__), 'pyblog.db')

# Create a database object
db  = flask_sqlalchemy.SQLAlchemy(app)

# Create migration object
migrate = flask_migrate.Migrate(app, db)


from pyblog import routes, models
