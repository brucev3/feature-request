from flask import Blueprint, render_template
from my_app import manager
from my_app.features.models import Feature, Customer
from my_app.decorators import template_or_json

# Flask-Restless - db only - implicit routes ~/api/<db.model.classname>
manager.create_api(Feature, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Customer, methods=['GET', 'POST', 'DELETE'])
# can use custom processors to customize handling of the requests
# see  -  https://flask-restless.readthedocs.io/en/latest/processors.html

features = Blueprint('features', __name__)

@features.route('/')
@features.route('/home')
def home():
    features = Feature.query.all()
    return render_template('home.html')
    # return {'count': len(features)} # TODO future feature for RESTfulness
