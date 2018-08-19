from flask import Flask
#from flask_restful import Api
# from flask_restless import APIManager # TODO future feature for RESTfulness
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///features.db'  # local location
db = SQLAlchemy(app)

# # Flask-Restless - db only - implicit routes ~/api/<db.model.classname>
# manager = APIManager(app, flask_sqlalchemy_db=db)  # TODO future feature for RESTfulness

from my_app.features.views import featreq

app.register_blueprint(featreq)

# db.drop_all()
# db.create_all()

app.secret_key = 'some_secret_key'