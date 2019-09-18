from pyblog import db

class User(db.Model):

    id        = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))
    age     = db.Column(db.Integer, default=0)
    email = db.Column(db.String(512))
    city     = db.Column(db.String(64))

    def __repr__(self):
        return "<User {}>".format(self.name)
