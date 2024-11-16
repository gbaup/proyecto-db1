from src.config.db import get_db_connection


def crear_clase(ci_instructor, id_actividad, id_turno):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO clase (ci_instructor, id_actividad, id_turno, dictada) VALUES (%s, %s, %s, false)",
            (ci_instructor, id_actividad, id_turno))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al crear la clase: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Clase creada exitosamente"}
