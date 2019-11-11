#################################################
#######                                   #######
#######             __INIT__.PY           #######
#######                                   ####### 
#################################################

import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
import os

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'youwillneverguess'

# Define the path of the database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ os.path.join(os.path.dirname(__file__),
                                                                   'payment.db')

# Create a database object
db  = flask_sqlalchemy.SQLAlchemy(app)

# Create migration object
migrate = flask_migrate.Migrate(app, db)

# Create a login manager object
login_mngr = flask_login.LoginManager(app)

from payment_app import routes, models
