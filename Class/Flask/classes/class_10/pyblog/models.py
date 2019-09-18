from pyblog import db
from werkzeug import security

class User(db.Model):

    id                  = db.Column(db.Integer(), primary_key=True)
    name            = db.Column(db.String(64))
    age                 = db.Column(db.Integer, default=0)
    email             = db.Column(db.String(512))
    city                 = db.Column(db.String(64))
    pwd_hash    = db.Column(db.String(254))

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
        # Retrieve user
        user = cls.query.filter_by(name=username).first()
        if not user:
            return False

        # Checking his password
        return user.check_password

    def __repr__(self):
        return "<User {}>".format(self.name)

