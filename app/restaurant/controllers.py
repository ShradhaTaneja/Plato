from flask import Blueprint

api = Blueprint('restaurant', __name__, url_prefix = '/restaurant')

@api.route('/test', methods=['GET'])
def test():
    return 'test from controller'
