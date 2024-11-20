from flask import Blueprint, request, jsonify
from src.services.clases_service import *

clases_bp = Blueprint('clases_bp', __name__)


@clases_bp.route('/clases', methods=['POST'])
def add_clase():
    data = request.get_json()
    ci_instructor = data.get('ci_instructor')
    id_actividad = data.get('id_actividad')
    id_turno = data.get('id_turno')

    result = create_clase(ci_instructor, id_actividad, id_turno)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200


@clases_bp.route('/clases/<int:id>', methods=['PUT'])
def modifify_clase(id):
    data = request.get_json()
    ci_instructor = data.get('ci_instructor')
    id_turno = data.get('id_turno')

    result = edit_clase(id, ci_instructor, id_turno)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200


@clases_bp.route('/clases/nuevoalumno', methods=['POST'])
def inscribir_alumno():
    data = request.get_json()
    ci_alumno = data.get('ci_alumno')
    id_clase = data.get('id_clase')
    id_equipo = data.get('id_equipo')

    result = add_alumno_a_clase(ci_alumno, id_clase, id_equipo)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200


@clases_bp.route('/clases/borraralumno', methods=['DELETE'])
def desinscribir_alumno():
    data = request.get_json()
    ci_alumno = data.get('ci_alumno')
    id_clase = data.get('id_clase')

    result = remove_alumno_de_clase(ci_alumno, id_clase)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200
