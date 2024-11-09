from src.config.db import get_db_connection


def fetch_logins():
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM login")
        logins = cursor.fetchall()
    except Exception as e:
        return {"error": f"Error al ejecutar la consulta: {e}"}
    finally:
        cursor.close()
        connection.close()

    return logins
