from flask import Blueprint, jsonify, request
from app.commons.modules import restaurant as module
from werkzeug.datastructures import CombinedMultiDict

api = Blueprint('restaurant', __name__, url_prefix = '/restaurant')

@api.route('/test', methods=['GET'])
def test():
    return 'test from controller'

@api.route('/', methods=['GET'])
@api.route('/<rid>', methods=['GET'])
def get_all(rid = None):
    if rid is None:
        all_data = module.get_all_restaurants()
    else:
        print 'inside controller, rid given calling get rest'
        all_data = module.get_restaurant(rid)
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

@api.route('/delete/<rid>', methods=['GET'])
def delete_restaurant(rid):
    all_data = module.remove_restaurant(rid)
    return jsonify(all_data)
