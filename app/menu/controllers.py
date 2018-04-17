from flask import Blueprint, jsonify, request
from app.commons.modules import menu as module
from werkzeug.datastructures import CombinedMultiDict

api = Blueprint('menu', __name__, url_prefix = '/menu')

@api.route('/test', methods=['GET'])
def test():
    return 'test from controller'

@api.route('/', methods = ['GET'])
@api.route('/<rid>', methods=['GET'])
@api.route('/<rid>/<mid>', methods=['GET'])
def get_all(rid = None, mid = None):
    if rid is None:
        return jsonify({
            'status' : 'failure',
            'message' : 'missing restaurant id..!'
            })
    if mid is None:
        all_data = module.get_all_menu(int(rid))
    else:
        all_data = module.get_specific_menu(int(rid), mid)
    return jsonify(all_data)

@api.route('/add', methods=['POST'])
def add_restaurant():
    required_parameters = ['name', 'address', 'city', 'state', 'contact']
    incoming_data = dict(request.get_json())
    incoming_parameters = incoming_data.keys()

    if len(set(required_parameters) - set(incoming_parameters)) > 0:
        return jsonify({
                'status' : 'failure',
                'message' : 'missing parameters.. you need to give it ALL.. :P (%s)' % (', '.join(required_parameters))
                })

    response = module.add_restaurant(incoming_data)
    return jsonify(response)
