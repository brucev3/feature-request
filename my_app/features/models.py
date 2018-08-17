from my_app import db

# https://media.readthedocs.org/pdf/flask-restless/latest/flask-restless.pdf
# Create your Flask-SQLALchemy models as usual but with the following
# restriction: they must have an __init__ method that accepts keyword
# arguments for all columns (the constructor in
# flask_sqlalchemy.SQLAlchemy.Model supplies such a method, so you
# don't need to declare a new one).
class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    priority = db.Column(db.Integer)
    description = db.Column(db.String(2048))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship(
        'Customer', backref=db.backref('features', lazy='dynamic')
    )

    def __repr__(self):
        return '<Feature %d>' % self.id

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return '<Customer %d>' % self.id
