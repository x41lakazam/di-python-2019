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
    return "Hello world"

