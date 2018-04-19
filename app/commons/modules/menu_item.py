import app.menu_item.models as model
from app.commons.modules import menu
from random import randint

def get_all_menu_items(rid):
    response = {}
    try:
        data = model.fetch_all_menu_items(rid)
        response['status'] = 'success'
        response['data'] = data
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response

def get_category_menu_items(rid, category):
    response = {}
    try:
        data = model.fetch_category_menu_items(rid, category)
        response['status'] = 'success'
        response['data'] = data
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response

def get_item(rid, item_id):
    response = {}
    try:
        data = model.fetch_item(rid, item_id)
        response['status'] = 'success'
        response['data'] = data
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response

def add_menu_item(data):
    response = {}
    if not menu.rest_category_exists(data['rid'], data['category']):
        return {'status': 'failure', 'message': 'either restaurant or category is invalid'}

    item_id = '%d-%s-%d' % (data['rid'], data['category'][0:3].upper(), randint(1000, 9999))
    data['item_id'] = item_id
    try:
        model.insert_menu_item(data)
        response['status'] = 'success'
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response

def remove_menu_item(rid, mcategory, item_id):
    response = {}
    try:
        model.delete_menu_item(rid, mcategory, item_id)
        response['status'] = 'success'
    except Exception as e:
        response['status'] = 'failure'
        response['message'] = str(e)
    return response
