from flask import Blueprint, jsonify, request
from app.commons.modules import menu_item as module
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
