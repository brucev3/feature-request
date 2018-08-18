from my_app import db
from my_app.features.models import populate

db.create_all()
populate()
