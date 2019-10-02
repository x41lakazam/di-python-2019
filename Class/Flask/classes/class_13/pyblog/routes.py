###################################################
######                                                                                                      ######
######            pyblog/routes.py                                                            ######
######                                                                                                       ######
###################################################

from pyblog import fake_data
from pyblog import app, db, login_mngr
from pyblog import forms, models
import flask
import datetime
import flask_login
from werkzeug import security

@app.route('/')
@app.route('/home')
def homepage():
    if flask_login.current_user.is_anonymous:
        d = datetime.datetime.now()
        current_date = "{}/{}/{}".format(d.day, d.month, d.year)

        return flask.render_template("home.jin", today_date=current_date)
    else:
        return flask.redirect(flask.url_for('user_profile', user_id=flask_login.current_user.id ))


@app.route('/contact')
def contact():
    return flask.render_template("contact.jin")


@app.route('/users')
def users_list():
    all_users = models.User.query.all()
    for user in all_users:
        if flask_login.current_user.is_authenticated and user.id == flask_login.current_user.id:
            all_users.remove(user)

    return flask.render_template('users_list.jin',
                                 users=all_users)


@app.route('/user_profile/<user_id>')
def user_profile(user_id):
    found = models.User.query.get(user_id)

    if found:
        user_posts = found.posts
        return flask.render_template('user_profile.jin', user=found, posts=user_posts)
    else:
        return flask.redirect(flask.url_for('homepage'))

@app.route("/sign_in", methods=('GET','POST'))
def signin():
    form = forms.SignIn()
    if flask.request.method == "GET":
        return flask.render_template('signin.jin', signinform=form)

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = models.User.check_signin(username, password)
        if user:
            flask.flash("{} logged in !".format(username))
            flask_login.login_user(user)
        else:
            flask.flash("Invalid username/password combination")
            return flask.redirect(flask.url_for('signin'))

    else:
        flask.flash("Invalid form!")
        return flask.render_template('signin.jin', signinform=form)
    return flask.redirect(flask.url_for('homepage'))

@app.route("/sign_up", methods=('GET', 'POST'))
def signup():
    form = forms.Signup()

    if flask.request.method == "GET":  # STATE 1: The user requests only the html content
        return flask.render_template("signup.jin", signupform=form)

    else:  # STATE 2: The user already saw the page and filled the content

        if form.validate_on_submit():  # STATE 2a: The form is valid

            # Create a user
            user = models.User()
            user.name = form.username.data
            user.age = form.age.data
            user.email =   form.email.data
            user.city = form.city.data

            user.add_password(form.password.data)

            user.add_to_db()

            flask.flash("Welcome, " + form.username.data)
            return flask.redirect(flask.url_for('homepage'))

        else:  # STATE 2b: The form is invalid
            flask.flash("Invalid form")
            return flask.render_template("signup.jin", signupform=form)

@app.route("/sign-out")
def signout():
    # log the user out
    flask_login.logout_user()

    # Redirect somewhere
    return flask.redirect(flask.url_for('homepage'))

@flask_login.login_required
@app.route("/new-post", methods=("GET","POST"))
def newpost():
    form = forms.NewPost()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        # Create a post
        post = models.Post()

        # Add attributes
        post.title = title
        post.content = content

        # Link to a user
        post.author = flask_login.current_user

        # Retrieve and add tags
        post.add_tags_from_content()

        flask.flash("{} Added a post".format(flask_login.current_user.name))
       # Save
        db.session.commit()

        return flask.redirect(flask.url_for("homepage"))
    return flask.render_template("new_post.jin", form=form)

