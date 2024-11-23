from flask import Flask
from flask_cors import CORS
from src.controllers.login_controller import *
from src.controllers.instructores_controller import *
from src.controllers.turnos_controller import *
from src.controllers.alumnos_controller import *
from src.controllers.actividades_controller import *
from src.controllers.clases_controller import *
from src.controllers.metricas_controller import *


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(login_bp, url_prefix='/api')
    app.register_blueprint(instructor_bp, url_prefix='/api')
    app.register_blueprint(turnos_bp, url_prefix='/api')
    app.register_blueprint(alumnos_bp, url_prefix='/api')
    app.register_blueprint(actividades_bp, url_prefix='/api')
    app.register_blueprint(clases_bp, url_prefix='/api')
    app.register_blueprint(metricas_bp, url_prefix='/api')

    return app
