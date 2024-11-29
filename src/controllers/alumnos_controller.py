from flask import Blueprint, request, jsonify
from src.services.alumnos_service import *

alumnos_bp = Blueprint('alumnos_bp', __name__)


@alumnos_bp.route('/alumnos', methods=['POST'])
def add_alumno():
    data = request.get_json()
    ci = data.get('ci')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    fecha_nacimiento = data.get('fecha_nacimiento')
    mail = data.get('mail')
    telefono = data.get('telefono')

    if not ci or not nombre or not apellido or not fecha_nacimiento or not mail or not telefono:
        return jsonify({
            "error": "Faltan campos obligatorios: 'ci', 'nombre', 'apellido', 'fecha_nacimiento', 'mail', 'telefono"}), 400

    result = create_alumno(ci, nombre, apellido, fecha_nacimiento, mail, telefono)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 201


@alumnos_bp.route('/alumnos/<int:ci>', methods=['PUT'])
def modify_alumno(ci):
    data = request.get_json()
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    fecha_nacimiento = data.get('fecha_nacimiento')
    mail = data.get('mail')
    telefono = data.get('telefono')

    if not ci:
        return jsonify({"error": "Falta la ci del alumno"}), 400

    result = edit_alumno(ci, nombre, apellido, fecha_nacimiento, mail, telefono)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200


@alumnos_bp.route('/alumnos/<int:ci>', methods=['DELETE'])
def remove_alumno(ci):
    if not ci:
        return jsonify({"error": "Falta la ci del alumno"}), 400

    result = delete_alumno(ci)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200
