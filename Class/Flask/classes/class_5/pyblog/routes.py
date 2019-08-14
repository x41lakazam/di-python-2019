###################################################
######                                       ######
######            pyblog/routes.py           ###### 
######                                       ######
###################################################

from pyblog import fake_data
from pyblog import app
import flask
import datetime

@app.route('/')
@app.route('/home')
def homepage():
    d            = datetime.datetime.now()
    current_date = "{}/{}/{}".format(d.day, d.month, d.year)

    return flask.render_template("home.jin", today_date=current_date)

@app.route('/contact')
def contact():
    return flask.render_template("contact.jin")

@app.route('/users')
def users_list():
    return flask.render_template('users_list.jin',
                                users=fake_data.users)

@app.route('/user_profile/<username>')
def user_profile(username):
    found = None
    for user in fake_data.users:
        if user.username.lower() == username.lower():
            found = user
 
    if found:
        return flask.render_template('user_profile.jin', user=found)
    else:
        return flask.redirect(flask.url_for('homepage'))


