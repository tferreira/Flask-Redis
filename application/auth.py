from functools import wraps
from flask import request, jsonify
from index import app


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', None)
        if token == app.config['SECRET_KEY']:
            return f(*args, **kwargs)

        return jsonify(message="Authentication is required to access this resource"), 401

    return decorated
