from flask import Blueprint, request, jsonify
from src.services.instructores_service import *

instructor_bp = Blueprint('instructor_bp', __name__)


@instructor_bp.route('/instructor', methods=['POST'])
def add_instructor():
    data = request.get_json()
    ci = data.get('ci')
    nombre = data.get('nombre')
    apellido = data.get('apellido')

    if not ci or not nombre or not apellido:
        return jsonify({"error": "Faltan campos obligatorios: 'ci', 'nombre', 'apellido'"}), 400

    result = create_instructor(ci, nombre, apellido)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 201


@instructor_bp.route('/instructor', methods=['PUT'])
def modify_instructor():
    data = request.get_json()
    ci = data.get('ci')
    nombre = data.get('nombre')
    apellido = data.get('apellido')

    if not ci:
        return jsonify({"error": "Faltan la ci del instructor"}), 400

    result = edit_instructor(ci, nombre, apellido)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200


@instructor_bp.route('/instructor/<int:id>', methods=['DELETE'])
def remove_instructor(ci):
    if not ci:
        return jsonify({"error": "Falta la ci del instructor"}), 400

    result = delete_instructor(ci)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200
