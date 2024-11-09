from flask import Flask
from flask_cors import CORS
from src.controllers.login_controller import *
from src.controllers.instructores_controller import *


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(login_bp, url_prefix='/api')
    app.register_blueprint(instructor_bp, url_prefix='/api')

    return app
