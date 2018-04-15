import app.restaurant.models as model

def get_all_restaurants():
    response = {}
    try:
        data = model.fetch_all_restaurants()
        response['status'] = 'success'
        response['data'] = data
    except:
        response['status'] = 'failure'
        response['data'] = None
    return response


def get_restaurant(rid):
    response = {}
    try:
        data = model.fetch_restaurant(rid)
        response['status'] = 'success'
        response['data'] = data
    except Exception as e:
        response['status'] = 'failure'
        response['data'] = None
        response['message'] = str(e)
    return response
