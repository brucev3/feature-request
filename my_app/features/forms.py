from flask_wtf import Form
from wtforms import TextField, DecimalField, SelectField, FileField
from wtforms.validators import InputRequired, NumberRange, Optional, ValidationError
from wtforms.widgets import Select, html_params, HTMLString
from my_app.features.models import Client, Area
from decimal import Decimal # TODO temporary

### Forms ###
# https://wtforms.readthedocs.io/en/latest/widgets.html
class CustomClientInput(Select): # custom radio button widget

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        html = []
        for val, label, selected in field.iter_choices():
            html.append(
                '<input type="radio" %s> %s' % (
                    html_params(
                        name=field.name, value=val, checked=selected, **kwargs
                    ), label
                )
            )
        return HTMLString(' '.join(html))

class ClientField(SelectField): # custom field
    widget = CustomClientInput()

    def iter_choices(self):
        clients = [(c.id, c.name) for c in Client.query.all()]
        for value, label in clients:
            yield (value, label, self.coerce(value) == self.data)

    def pre_validate(self, form):

        for v, _ in [(c.id, c.name) for c in Client.query.all()]:
            if self.data == v:
                break
            else:
                pass
                # raise ValueError(self.gettext('Not a valid choice')) # TODO this needs work

class AreaField(SelectField): # custom field
    widget = CustomClientInput()

    def iter_choices(self):
        areas = [(c.id, c.name) for c in Area.query.all()]
        for value, label in areas:
            yield (value, label, self.coerce(value) == self.data)

    def pre_validate(self, form):

        for v, _ in [(c.id, c.name) for c in Client.query.all()]:
            if self.data == v:
                break
            else:
                pass

class FeatureForm(Form):
    title = TextField('Title', validators=[InputRequired()])
    client = ClientField(
        'Client', validators=[InputRequired()], coerce=int
    )
    area = AreaField(
        "Product Area", validators=[InputRequired()], coerce=int
    )
    priority = DecimalField('Priority', validators=[
        InputRequired(), NumberRange(min=Decimal('0.0'))
    ])
