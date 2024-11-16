from src.config.db import get_db_connection


def create_turno(hora_inicio, hora_fin):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO turnos (hora_inicio, hora_fin) VALUES (%s, %s)", (hora_inicio, hora_fin))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al crear el turno: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Turno creado exitosamente"}


def edit_turno(id, hora_inicio, hora_fin):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE turnos SET hora_inicio = %s, hora_fin = %s WHERE id = %s", (hora_inicio, hora_fin, id))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al modificar el turno: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Turno modificado exitosamente"}


def delete_turno(id):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM turnos WHERE id = %s", (id,))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al eliminar el turno: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Turno eliminado exitosamente"}
