from flask import Blueprint, render_template
# from my_app import manager # TODO future feature for RESTfulness
from my_app import app
from my_app.features.models import Feature, Area, Client
from my_app.decorators import template_or_json

# # Flask-Restless - db only - implicit routes ~/api/<db.model.classname>
# manager.create_api(Feature, methods=['GET', 'POST', 'DELETE']) # TODO future feature for RESTfulness
# manager.create_api(Customer, methods=['GET', 'POST', 'DELETE']) # TODO future feature for RESTfulness
# # can use custom processors to customize handling of the requests
# # see  -  https://flask-restless.readthedocs.io/en/latest/processors.html

featreq = Blueprint('features', __name__)

@featreq.route('/')
@featreq.route('/home')
@template_or_json('home.html')
def home():
    # return render_template('home.html')
    fs = Feature.query.all()
    return {'count': len(fs)}

@featreq.route('/feature/<id>')
def feature(id):
    f = Feature.query.get_or_404(id)
    return render_template('feature.html', feature=f)


@featreq.route('/features/')
@featreq.route('/features/<int:page>')
def features(page=1):
    fs = Feature.query.paginate(page, 10)
    return render_template('features.html', features=fs)





@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
