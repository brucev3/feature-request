from my_app import db

# https://media.readthedocs.org/pdf/flask-restless/latest/flask-restless.pdf
# Create your Flask-SQLALchemy models as usual but with the following
# restriction: they must have an __init__ method that accepts keyword
# arguments for all columns (the constructor in
# flask_sqlalchemy.SQLAlchemy.Model supplies such a method, so you
# don't need to declare a new one).
class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(2048))
    client_priority = db.Column(db.Integer)
    target_date = db.Column(db.Date)

    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    area = db.relationship(
        'Area', backref=db.backref('features', lazy='dynamic')
    )

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship(
        'Client', backref=db.backref('features', lazy='dynamic')
    )

    def __repr__(self):
        return '<Feature %d>' % self.id

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(50))

    def __repr__(self):
        return '<Area %d>' % self.id

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return '<Client %d>' % self.id
