from flask import Blueprint, request, jsonify
from src.services.turnos_service import *

turnos_bp = Blueprint('turnos_bp', __name__)


@turnos_bp.route('/turnos', methods=['POST'])
def add_turno():
    data = request.get_json()
    hora_inicio = data.get('hora_inicio')
    hora_fin = data.get('hora_fin')

    if not hora_inicio or not hora_fin:
        return jsonify({"error": "Faltan campos obligatorios: 'hora_inicio', 'hora_fin'"}), 400

    result = create_turno(hora_inicio, hora_fin)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 201


@turnos_bp.route('/turnos', methods=['PUT'])
def modify_turno():
    data = request.get_json()
    id = data.get('id')
    hora_inicio = data.get('hora_inicio')
    hora_fin = data.get('hora_fin')

    if not id or not hora_inicio or not hora_fin:
        return jsonify({"error": "Faltan campos obligatorios: 'id', 'hora_inicio', 'hora_fin'"}), 400

    result = edit_turno(id, hora_inicio, hora_fin)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200


@turnos_bp.route('/instructor', methods=['DELETE'])
def remove_turno():
    data = request.get_json()
    id = data.get('id')

    if not id:
        return jsonify({"error": "Falta el d id el turno"}), 400

    result = delete_turno(id)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200
