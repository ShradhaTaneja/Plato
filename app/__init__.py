from flask import Flask

app = Flask(__name__)

from app.restaurant.controllers import api as restaurant_api

app.register_blueprint(restaurant_api)


