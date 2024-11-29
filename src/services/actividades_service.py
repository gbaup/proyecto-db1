from src.config.db import get_db_connection


def edit_actividad(id, descripcion=None, costo=None):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()

        fields_to_update = []
        values = []

        if descripcion is not None:
            fields_to_update.append("descripcion = %s")
            values.append(descripcion)
        if costo is not None:
            fields_to_update.append("costo = %s")
            values.append(costo)

        if not fields_to_update:
            return {"error": "No se proporcionaron campos para actualizar"}

        values.append(id)

        query = f"UPDATE actividades SET {', '.join(fields_to_update)} WHERE id = %s"
        cursor.execute(query, tuple(values))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al modificar la actividad: {e}"}
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return {"message": "Actividad modificada exitosamente"}


def get_actividades():
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM actividades")
        actividades = cursor.fetchall()

    except Exception as e:
        return {"error": f"Error al obtener las actividades: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"actividades": actividades}
