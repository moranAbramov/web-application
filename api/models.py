from api import db
from sqlalchemy import inspect


class People(db.Model):
    id: str
    title: str
    content: str
    viewes: int
    timestamp: int

    id = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    views = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Integer, primary_key=True)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return '<People %r>' % self.id
