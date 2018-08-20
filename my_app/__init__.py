from flask import Flask
# from flask_restless import APIManager # TODO future feature for RESTfulness
# from flask_restful import Api # TODO future feature for RESTfulness
from flask_sqlalchemy import SQLAlchemy

# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///features.db'  # local location
db = SQLAlchemy(application)

# # Flask-Restless - db only - implicit routes ~/api/<db.model.classname>
# manager = APIManager(app, flask_sqlalchemy_db=db)  # TODO future feature for RESTfulness
# # Flask-Restful - explicit routes defined with api.add_resource()
# api = Api(app) # TODO future feature for RESTfulness

from my_app.features.views import featreq

application.register_blueprint(featreq)

# db.drop_all()
# db.create_all()

application.secret_key = 'some_secret_key'