import flask_wtf
import wtforms
from wtforms import validators as valid

class Signup(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username", validators=[valid.DataRequired(message="Username can't be empty")])
    email          = wtforms.StringField("Email", validators=[valid.DataRequired(), valid.Email()])
    password   = wtforms.PasswordField("Password", validators=[valid.DataRequired()])
    password_confirm   = wtforms.PasswordField("Confirm password", validators=[valid.DataRequired(),
                                                                                                                                                                    valid.EqualTo('password')])
    submit          = wtforms.SubmitField("Sign up")