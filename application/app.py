from flask import jsonify
from index import app  # , db
from .auth import requires_auth
# from .models import MyObject


@app.route('/api/status', methods=['GET'])
def index():
    return jsonify({'status': 'ok'})


@app.route("/api/auth", methods=["GET"])
@requires_auth
def check_auth():
    return jsonify({'status': 'ok'})
