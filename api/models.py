from api import db


class People(db.Model):
    id = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(80), unique=True, nullable=False)
    views = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<People %r>' % self.id
