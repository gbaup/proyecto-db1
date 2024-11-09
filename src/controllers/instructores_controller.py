from flask import Blueprint, request, jsonify
from src.services.instructores_service import create_instructor

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
