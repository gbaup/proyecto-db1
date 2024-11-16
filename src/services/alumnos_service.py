from src.config.db import get_db_connection


def create_alumno(ci, nombre, apellido, fecha_nacimiento, mail, telefono):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento, mail, telefono) VALUES (%s, %s, %s, %s, %s, %s)",
            (ci, nombre, apellido, fecha_nacimiento, mail, telefono))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al crear el turno: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Alumno creado exitosamente"}


def edit_alumno(ci, nombre, apellido, fecha_nacimiento, mail, telefono):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE alumnos SET nombre = %s, apellido = %s, fecha_nacimiento = %s, mail = %s, telefono = %s WHERE ci = %s",
            (ci, nombre, apellido, fecha_nacimiento, mail, telefono))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al modificar el alumno: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Alumno modificado exitosamente"}


def delete_alumno(ci):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM alumnos WHERE ci = %s", (ci,))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al eliminar el alumno: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Alumno eliminado exitosamente"}
