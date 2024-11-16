from flask import Blueprint, request, jsonify
from src.services.alumnos_service import *

alumnos_bp = Blueprint('alumnos_bp', __name__)


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


def modify_alumno():
    data = request.get_json()
    ci = data.get('ci')
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


def remove_alumno():
    data = request.get_json()
    ci = data.get('ci')

    if not ci:
        return jsonify({"error": "Falta la ci del alumno"}), 400

    result = delete_alumno(ci)

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200
