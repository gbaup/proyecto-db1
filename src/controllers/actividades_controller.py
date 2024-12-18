from flask import Blueprint, request, jsonify
from src.services.actividades_service import *

actividades_bp = Blueprint('actividades_bp', __name__)


@actividades_bp.route('/actividades', methods=['GET'])
def getAll_actividades():
    result = get_actividades()

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200


@actividades_bp.route('/actividades/<int:id>', methods=['PUT'])
def modify_actividad(id):
    data = request.get_json()
    descripcion = data.get('descripcion')
    costo = data.get('costo')

    if not id or not descripcion or not costo:
        return jsonify({"error": "Faltan campos obligatorios: 'id', 'descripcion', 'hora_fin'"}), 400

    result = edit_actividad(id, descripcion, costo)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200
