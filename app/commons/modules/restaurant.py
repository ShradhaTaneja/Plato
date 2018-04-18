import app.restaurant.models as model

def get_all_restaurants():
    response = {}
    try:
        data = model.fetch_all_restaurants()
        response['status'] = 'success'
        response['data'] = data
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response

def exists(rid):
    return model.exists(rid)

def get_restaurant(rid):
    response = {}
    data = model.fetch_restaurant(rid)
    try:
        data = model.fetch_restaurant(rid)
        if data == {}:
            return {'status': 'failure', 'message': 'restaurant doesn\'t exist'}
        response['status'] = 'success'
        response['data'] = data
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response

def add_restaurant(data):
    response = {}
    try:
        rid = model.insert_restaurant(data)
        response['status'] = 'success'
        response['data'] = {'rid' : rid}
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response




def remove_restaurant(rid):
    response = {}
    try:
        model.delete_restaurant(rid)
        response['status'] = 'success'
    except Exception as e:
        response['status'] = 'failure'
        response['message'] = str(e)
    return response
