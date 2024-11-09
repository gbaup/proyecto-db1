from flask import jsonify
from src.config.db import get_db_connection


def get_logins():
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM login")
        logins = cursor.fetchall()
    except Error as e:
        return jsonify({"error": f"Error al ejecutar la consulta: {e}"}), 500
    finally:
        cursor.close()
        connection.close()

    return jsonify(logins)
