###################################################
######                                                                                                      ######
######            pyblog/routes.py                                                            ######
######                                                                                                       ######
###################################################

from pyblog import fake_data
from pyblog import app
from pyblog import forms
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

@app.route("/sign_up",  methods=('GET', 'POST'))
def signup():
    form = forms.Signup()

    if flask.request.method == "GET":     # STATE 1: The user requests only the html content
        return flask.render_template("signup.jin", signupform=form)

    else:                # STATE 2: The user already saw the page and filled the content

        if form.validate_on_submit():                                                        # STATE 2a: The form is valid
            user = fake_data.User(username=form.username.data, email=form.email.data)
            fake_data.users.append(user)
            flask.flash("Welcome, "+ form.username.data)
            return flask.redirect(flask.url_for('homepage'))

        else:                                                                                                          # STATE 2b: The form is invalid
            flask.flash("Invalid form")
            return flask.render_template("signup.jin", signupform=form)
