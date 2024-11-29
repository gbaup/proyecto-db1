from datetime import datetime
from src.utils.utils import validar_cedula
from src.config.db import get_db_connection


def create_alumno(ci, nombre, apellido, fecha_nacimiento, mail, telefono):
    if validar_cedula(ci) is False:
        return {"error": "Cédula inválida"}

    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").strftime("%Y-%m-%d")
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


def edit_alumno(ci, nombre=None, apellido=None, fecha_nacimiento=None, mail=None, telefono=None):
    if validar_cedula(ci) is False:
        return {"error": "Cédula inválida"}

    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()

        fields_to_update = []
        values = []

        if nombre is not None:
            fields_to_update.append("nombre = %s")
            values.append(nombre)
        if apellido is not None:
            fields_to_update.append("apellido = %s")
            values.append(apellido)
        if fecha_nacimiento is not None:
            fields_to_update.append("fecha_nacimiento = %s")
            values.append(fecha_nacimiento)
        if mail is not None:
            fields_to_update.append("mail = %s")
            values.append(mail)
        if telefono is not None:
            fields_to_update.append("telefono = %s")
            values.append(telefono)

        if not fields_to_update:
            return {"error": "No se proporcionaron campos para actualizar"}

        values.append(ci)

        query = f"UPDATE alumnos SET {', '.join(fields_to_update)} WHERE ci = %s"
        cursor.execute(query, tuple(values))
        connection.commit()

    except Exception as e:
        return {"error": f"Error al modificar el alumno: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Alumno modificado exitosamente"}


def delete_alumno(ci):
    if validar_cedula(ci) is False:
        return {"error": "Cédula inválida"}

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
