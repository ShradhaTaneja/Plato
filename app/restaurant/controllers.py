from flask import Blueprint, jsonify
from app.commons.modules import restaurant as rest

api = Blueprint('restaurant', __name__, url_prefix = '/restaurant')

@api.route('/test', methods=['GET'])
def test():
    return 'test from controller'

@api.route('/', methods=['GET'])
def get_all():
    all_data = rest.get_all_restaurants()
    return jsonify(all_data)


