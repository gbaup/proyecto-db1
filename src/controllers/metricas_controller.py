from flask import Blueprint, request, jsonify
from src.services.metricas_service import *

metricas_bp = Blueprint('metricas_bp', __name__)


@metricas_bp.route('/metricas/clasemasconcurrida', methods=['GET'])
def clase_mas_concurrida():
    result = get_clase_mas_concurrida()

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200


@metricas_bp.route('/metricas/clasemasrentable', methods=['GET'])
def clase_mas_rentable():
    result = get_clase_mas_rentable()

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200


@metricas_bp.route('/metricas/turnomaspopular', methods=['GET'])
def turno_mas_popular():
    result = get_turno_mas_popular()

    if 'error' in result:
        return jsonify(result), 500

    return jsonify(result), 200
