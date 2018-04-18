import app.menu.models as model
import app.restaurant.models as rest_model

def get_all_menu(rid):
    response = {}
    if not rest_model.exists(rid):
        response['status'] = 'failure'
        response['message'] = 'restuarant doesn\'t exist'
        return response
    try:
        data = model.fetch_all_menu(rid)
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

def remove_menu(rid, mcategory):
    response = {}
    try:
        model.delete_menu(rid, mcategory)
        response['status'] = 'success'
    except Exception as e:
        response['status'] = 'failure'
        response['message'] = str(e)
    return response
