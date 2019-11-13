import flask_wtf
import wtforms
from wtforms import validators as valid

class Signup(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username", validators=[valid.DataRequired(message="Username can't be empty")])
    email          = wtforms.StringField("Email", validators=[valid.DataRequired(), valid.Email()])
    password   = wtforms.PasswordField("Password", validators=[valid.DataRequired()])
    password_confirm   = wtforms.PasswordField("Confirm password", validators=[valid.DataRequired(),
                                                                                                                                                                    valid.EqualTo('password')])

    age             = wtforms.IntegerField("Age", validators=[valid.DataRequired(message="Age can't be empty")])
    city             = wtforms.StringField("City", validators=[])

    submit          = wtforms.SubmitField("Sign up")

class SignIn(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username", validators=[valid.DataRequired(message="Username can't be empty")])
    password   = wtforms.PasswordField("Password", validators=[valid.DataRequired()])
    submit          = wtforms.SubmitField("Sign up")

class NewPost(flask_wtf.FlaskForm):

    title        = wtforms.StringField("title", validators=[valid.DataRequired(message="Field can't be empty")])
    content = wtforms.StringField("Content", validators=[valid.DataRequired(message="Field can't be empty")])

    submit      = wtforms.SubmitField("Post")

class PasswordResetRequest(flask_wtf.FlaskForm):
    mail = wtforms.StringField("Email", validators=[valid.DataRequired(), valid.Email()])

    submit = wtforms.SubmitField("Request password reset")

class PasswordReset(flask_wtf.FlaskForm):
    password = wtforms.StringField("Password", validators=[valid.DataRequired()])
    password_confirm = wtforms.StringField("Confirm password", validators=[valid.EqualTo('password')])

    submit = wtforms.SubmitField("Request password reset")
