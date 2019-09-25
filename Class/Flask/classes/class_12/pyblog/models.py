from pyblog import db, login_mngr
from werkzeug import security
import flask_login
import datetime

@login_mngr.user_loader
def load_user(user_id):
    user_id = int(user_id)
    return User.query.get(user_id)

class User(flask_login.UserMixin, db.Model):

    id                  = db.Column(db.Integer(), primary_key=True)
    name            = db.Column(db.String(64))
    age                 = db.Column(db.Integer, default=0)
    email             = db.Column(db.String(512))
    city                 = db.Column(db.String(64))
    pwd_hash    = db.Column(db.String(254))

    posts           = db.relationship('Post', backref='author')

    def add_password(self, password):
        self.pwd_hash = security.generate_password_hash(password)

    def check_password(self, password):
        return security.check_password_hash(self.pwd_hash, password)

    def add_to_db(self):
        self.name = self.name.title()
        db.session.add(self)
        db.session.commit()

    @classmethod
    def check_signin(cls, username, password):
        username = username.title()
        # Retrieve user
        user = cls.query.filter_by(name=username).first()
        if not user:
            return False

        # Checking his password
        if user.check_password(password):
            return user
        return False

    def __repr__(self):
        return "<User {}>".format(self.name)


class Post(db.Model):

    id                  = db.Column(db.Integer, primary_key=True)

    title             = db.Column(db.String(128),)
    content     = db.Column(db.Text())
    pub_date = db.Column(db.DateTime(), default=datetime.datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def pub_date_as_str(self):
        return "{}/{}/{} at {}:{}".format(
            self.pub_date.day,
            self.pub_date.month,
            self.pub_date.year,
            self.pub_date.hour,
            self.pub_date.minute,
        )



