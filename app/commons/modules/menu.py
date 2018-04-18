import app.menu.models as model
import app.restaurant.models as rest_model


def rest_category_exists(rid, category):
    return model.rest_category_exists(rid, category)

def category_exists(category):
    return model.category_exists(category)

def get_categories():
    response = {}
    try:
        data = model.fetch_categories()
        response['status'] = 'success'
        response['data'] = data
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response


def get_menu(rid):
    response = {}
    if not rest_model.exists(rid):
        response['status'] = 'failure'
        response['message'] = 'restuarant doesn\'t exist'
        return response
    try:
        data = model.fetch_menu(rid)
        if data == {}:
            response['status'] = 'failure'
            response['message'] = 'no menu found'
            return response
        response['status'] = 'success'
        response['data'] = data
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response


def add_menu(rid, category):
    response = {}
    try:
        if not model.category_exists(category):
            model.insert_category(category)
        data = model.insert_menu(rid, category)
        response['status'] = 'success'
    except Exception as e:
        response['status'] = 'failure'
        response['message'] = str(e)
    return response



def remove_menu(rid, mcategory):
    response = {}
    try:
        model.delete_menu(rid, mcategory)
        response['status'] = 'success'
    except Exception as e:
        response['status'] = 'failure'
        response['message'] = str(e)
    return response
