from flask import Blueprint, jsonify, request
from app.commons.modules import menu as module
from app.commons.modules import restaurant
from werkzeug.datastructures import CombinedMultiDict

api = Blueprint('menu', __name__, url_prefix = '/menu')

@api.route('/test', methods=['GET'])
def test():
    return 'test from controller'

@api.route('/', methods = ['GET'])
@api.route('/all', methods=['GET'])
def get_categoreies():
    response = module.get_categories()
    return jsonify(response)

@api.route('/<rid>', methods=['GET'])
def get_menu(rid = None):
    if rid is None:
        return jsonify({
            'status' : 'failure',
            'message' : 'missing restaurant id..!'
            })
    all_data = module.get_menu(int(rid))
    return jsonify(all_data)

@api.route('/add', methods=['POST'])
def add_menu():
    incoming_data = dict(request.get_json())
    if 'category' not in incoming_data.keys() or 'rid' not in incoming_data.keys():
        return jsonify({
            'status' : 'failed',
            'message' : 'missing parameters.. please add category and rid'
            })
    if not restaurant.exists(incoming_data['rid']):
        return jsonify({
            'status' : 'failed',
            'message' : 'restaurant not found! please create a restaurant first'
            })
    response = module.add_menu(int(incoming_data['rid']), str(incoming_data['category']).lower())
    return jsonify(response)

@api.route('/delete', methods=['POST'])
def delete_menu():
    incoming_data = dict(request.get_json())
    if 'category' not in incoming_data.keys() or 'rid' not in incoming_data.keys():
        return jsonify({
            'status' : 'failed',
            'message' : 'missing parameters.. please add category and rid'
            })
    if not restaurant.exists(int(incoming_data['rid'])):
        return jsonify({
            'status' : 'failed',
            'message' : 'restaurant not found! please create a restaurant first'
            })
    if not module.rest_category_exists(int(incoming_data['rid']), str(incoming_data['category']).lower()):
        return jsonify({
            'status' : 'failed',
            'message' : 'invalid category, no such menu found for this restaurant'
            })
    all_data = module.remove_menu(int(incoming_data['rid']), str(incoming_data['category']).lower())
    return jsonify(all_data)
