from src.config.db import get_db_connection


def get_turnos():
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM turnos")
        turnos = cursor.fetchall()

    except Exception as e:
        return {"error": f"Error al obtener los turnos: {e}"}
    finally:
        cursor.close()
        connection.close()

    return turnos


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


def edit_turno(id, hora_inicio=None, hora_fin=None):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()

        fields_to_update = []
        values = []

        if hora_inicio is not None:
            fields_to_update.append("hora_inicio = %s")
            values.append(hora_inicio)
        if hora_fin is not None:
            fields_to_update.append("hora_fin = %s")
            values.append(hora_fin)

        if not fields_to_update:
            return {"error": "No se proporcionaron campos para actualizar"}

        values.append(id)

        query = f"UPDATE turnos SET {', '.join(fields_to_update)} WHERE id = %s"
        cursor.execute(query, tuple(values))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al modificar el turno: {e}"}
    finally:
        if cursor:
            cursor.close()
        if connection:
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
