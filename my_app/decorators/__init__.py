from flask import request, jsonify, render_template
from functools import wraps

# is_xhr decorator
def template_or_json(template=None): # TODO future feature for RESTfulness
    """"
    Return a dict from your view and this will either
    pass it to a template or render json. Use like:
    @template_or_json('template.html')

    :param  optional template to use if the request is not xhr
    """
    def decorated(f):
        @wraps(f)
        def decorated_fn(*args, **kwargs):
            ctx = f(*args, **kwargs)
            if request.is_xhr or not template:
                return jsonify(ctx)
            else:
                return render_template(template, **ctx)
        return decorated_fn
    return decorated
