from flask import Blueprint, jsonify
from src.services.login_service import fetch_logins

login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/login', methods=['GET'])
def get_logins():
    logins = fetch_logins()
    if isinstance(logins, dict) and "error" in logins:
        return jsonify(logins), 500
    return jsonify(logins)
