from src.config.db import get_db_connection
from src.utils.utils import validar_cedula


def create_instructor(ci, nombre, apellido):
    if validar_cedula(ci) is False:
        return {"error": "Cédula inválida"}

    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO instructores (ci, nombre, apellido) VALUES (%s, %s, %s)", (ci, nombre, apellido))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al crear el instructor: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Instructor creado exitosamente"}
