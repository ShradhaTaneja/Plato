from flask import Blueprint, jsonify
from app.commons.modules import restaurant as rest

api = Blueprint('restaurant', __name__, url_prefix = '/restaurant')

@api.route('/test', methods=['GET'])
def test():
    return 'test from controller'

@api.route('/', methods=['GET'])
@api.route('/<rid>', methods=['GET'])
def get_all(rid = None):
    if rid is None:
        all_data = rest.get_all_restaurants()
    else:
        all_data = rest.get_restaurant(rid)
    return jsonify(all_data)


