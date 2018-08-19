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

        client = Client.query.get_or_404(form.client.data)
        area = Area.query.get_or_404(
            form.area.data
        )
        title = form.title.data
        # description = form.description.data

        # priority = form.priority.data

        f = Feature(
            title=title,
            # priority=priority,
            client=client,
            area=area
        )
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
