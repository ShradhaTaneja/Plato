from flask import Flask

app = Flask(__name__)

from app.restaurant.controllers import api as restaurant_api
from app.menu.controllers import api as menu_api

app.register_blueprint(restaurant_api)
app.register_blueprint(menu_api)


