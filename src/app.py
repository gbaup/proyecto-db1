from flask import Flask
from flask_cors import CORS
from src.controllers.login_controller import *


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registro de rutas
    app.add_url_rule('/login', 'get_logins', get_logins, methods=['GET'])

    return app
