import app.restaurant.models as model

def get_all_restaurants():
    response = {}
    try:
        data = model.get_all_restaurants()
        response['status'] = 'success'
        response['data'] = data
    except:
        response['status'] = 'failure'
        response['data'] = None
    return response
