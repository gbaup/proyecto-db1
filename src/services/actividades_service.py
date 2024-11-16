from src.config.db import get_db_connection

def edit_actividad(id, descripcion, costo):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE actividades SET descripcion = %s, costo = %s WHERE id = %s", (descripcion, costo, id))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al modificar la actividad: {e}"}
    finally:
        cursor.close()
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