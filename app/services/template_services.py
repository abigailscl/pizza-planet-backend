import functools
from flask import jsonify, abort


def template_service(service):
    @functools.wraps(service)
    def decorated_function(*args, **kwargs):
        data, error = service(*args, **kwargs)
        if not data:
            abort(404)
        response = data if not error else {'error': error}
        return jsonify(response)
    return decorated_function
