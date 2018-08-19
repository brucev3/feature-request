from flask import Blueprint, render_template, request, redirect, flash, url_for
# from my_app import manager # TODO future feature for RESTfulness
from my_app import app, db
from my_app.features.models import Feature, Area, Client
from my_app.features.forms import FeatureForm
from my_app.decorators import template_or_json

# # Flask-Restless - db only - implicit routes ~/api/<db.model.classname>
# manager.create_api(Feature, methods=['GET', 'POST', 'DELETE']) # TODO future feature for RESTfulness
# manager.create_api(Client, methods=['GET', 'POST', 'DELETE']) # TODO future feature for RESTfulness
# manager.create_api(Area, methods=['GET', 'POST', 'DELETE']) # TODO future feature for RESTfulness
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

@featreq.route('/feature-create', methods=['GET', 'POST'])
def create_feature():
    form = FeatureForm(request.form, csrf_enabled=False)

    # clients = [(c.id, c.name) for c in Client.query.all()]
    # form.clients.choices = clients

    if form.validate_on_submit(): # this is a POST

        title = form.title.data
        client = Client.query.get_or_404(form.client.data)
        priority = form.priority.data
        target_date = form.target_date.data
        area = Area.query.get_or_404(form.area.data)
        description = form.description.data

        f = Feature(
            title=title,
            client=client,
            priority=priority,
            target_date=target_date,
            area=area,
            description=description
        )
        maybe_adjust_priority(f)
        db.session.add(f)
        db.session.commit()
        flash('The feature %s has been created' % title, 'success')
        return redirect(url_for('features.feature', id=f.id))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('feature-create.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def maybe_adjust_priority(new_feature):
    '''
    When adding a new feature, adjust the feature priorities if there is conflict
    with any of the existing features. Recursively check until all the lower
    priority features have been shifted to their next lower priority (higher number)
    :param: Feature object
    :return: None
    '''

    client_features = get_client_features(new_feature.client.name)

    for f in client_features:
        if f.priority == new_feature.priority and f is not new_feature:
            adjust_priorities(client_features, new_feature)

# there was a conflict, need to adjust priorities
def adjust_priorities(features, new_feature):
    new_priority = new_feature.priority
    for f in features:
        if f.priority == new_priority and f is not new_feature:
            f.priority += 1
            db.session.commit()
            maybe_adjust_priority(f)

# get the features for a client
def get_client_features(clientname):

    all_features = Feature.query.all()
    client_features = []
    for f in all_features:
        if f.client.name == clientname:
            client_features.append(f)

    return client_features
