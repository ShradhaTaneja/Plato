from flask import Blueprint, jsonify, request
from app.commons.modules import menu_item as module
from app.commons.modules import menu as menu
from werkzeug.datastructures import CombinedMultiDict

api = Blueprint('menu_item', __name__, url_prefix = '/menu_item')

@api.route('/test', methods=['GET'])
def test():
    return 'test from controller'

@api.route('/<rid>', methods=['GET'])
@api.route('/<rid>/<category>', methods = ['GET'])
def get_all(rid = None, category = None):
    if rid is None:
        return jsonify({
                'status' : 'failure',
                'message' : 'missing parameters.. you need to give rid, and category(optional)'
                })
    if category is None:
        all_data = module.get_all_menu_items(int(rid))
    else:
        all_data = module.get_category_menu_items(int(rid), str(category))
    return jsonify(all_data)


@api.route('/get_item/<rid>/<item_id>', methods = ['GET'])
def get_item(rid = None, item_id = None):
    if rid is None:
        return jsonify({
                'status' : 'failure',
                'message' : 'missing parameters.. you need to give rid, and category(optional)'
                })
    all_data = module.get_item(int(rid), str(item_id))
    return jsonify(all_data)

@api.route('/add', methods=['POST'])
def add_menu_item():
    required_parameters = ['rid', 'category', 'name', 'price']
    incoming_data = dict(request.get_json())
    incoming_parameters = incoming_data.keys()

    if len(set(required_parameters) - set(incoming_parameters)) > 0:
        return jsonify({
                'status' : 'failure',
                'message' : 'missing parameters.. you need to give it ALL.. :P (%s)' % (', '.join(required_parameters))
                })

    response = module.add_menu_item(incoming_data)
    return jsonify(response)


@api.route('/delete', methods=['POST'])
def delete_menu_item():
    incoming_data = dict(request.get_json())
    if 'category' not in incoming_data.keys() or 'rid' not in incoming_data.keys() or 'item_id' not in incoming_data.keys():
        return jsonify({
            'status' : 'failed',
            'message' : 'missing parameters.. please add category, item_id and rid'
            })
    if not menu.rest_category_exists(int(incoming_data['rid']), str(incoming_data['category']).lower()):
        return jsonify({
            'status' : 'failed',
            'message' : 'invalid inputs, no such menu found for this restaurant'
            })
    all_data = module.remove_menu_item(int(incoming_data['rid']), str(incoming_data['category']).lower(), str(incoming_data['item_id']))
    return jsonify(all_data)

