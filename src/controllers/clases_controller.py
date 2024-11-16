from flask import Blueprint, request, jsonify
from src.services.clases_service import *

clases_bp = Blueprint('clases_bp', __name__)


@clases_bp.route('/clases', methods=['POST'])
def nueva_clase():
    data = request.get_json()
    ci_instructor = data.get('ci_instructor')
    id_actividad = data.get('id_actividad')
    id_turno = data.get('id_turno')

    result = crear_clase(ci_instructor, id_actividad, id_turno)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200
