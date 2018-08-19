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
    description = db.Column(db.Text(2048))
    priority = db.Column(db.Integer)
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
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Area %d>' % self.id

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return '<Client %d>' % self.id

# populate 'static' tables
def populate():
    for client in ['Client A', 'Client B', 'Client C']:

        dup = False
        for c in Client.query.distinct(Client.name):
            if client == c.name:
                dup = True
                break
        if dup:
            continue

        c = Client(name=client)
        db.session.add(c)
        db.session.commit()

    for area in ['Policies', 'Billing', 'Claims', 'Reports']:

        dup = False
        for a in Area.query.distinct(Area.name):
            if area == a.name:
                dup = True
                break
        if dup:
            continue

        a = Area(name=area)
        db.session.add(a)
        db.session.commit()

    # TODO possibly make populate cooler with --- $ sqlite3 features.db < features.sql
