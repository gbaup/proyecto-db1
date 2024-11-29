from src.config.db import get_db_connection
from datetime import datetime
from src.utils.utils import validar_cedula


def create_clase(ci_instructor, id_actividad, id_turno):
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


def edit_clase(id, ci_instructor, id_turno):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    if validar_cedula(ci_instructor) is False:
        return {"error": "Cédula inválida"}

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE clase 
            JOIN turnos ON clase.id_turno = turnos.id
            SET clase.ci_instructor = %s, clase.id_turno = %s 
            WHERE clase.id = %s 
              AND CURRENT_TIME() > turnos.hora_fin
            """,
            (ci_instructor, id_turno, id)
        )

        if cursor.rowcount == 0:
            return {"error": "La hora actual debe ser mayor a la hora de fin del turno, o el turno/clase no existe"}

        connection.commit()

    except Exception as e:
        return {"error": f"Error al modificar la clase: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Clase modificada exitosamente"}


def add_alumno_a_clase(ci_alumno, id_clase, id_equipo):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT 
                (SELECT id_turno FROM clase WHERE id = %s) AS turno_clase,
                EXISTS(
                    SELECT 1 
                    FROM alumno_clase ac
                    JOIN clase c ON ac.id_clase = c.id
                    WHERE ac.ci_alumno = %s AND c.id_turno = (SELECT id_turno FROM clase WHERE id = %s)
                ) AS conflicto
            """,
            (id_clase, ci_alumno, id_clase)
        )
        result = cursor.fetchone()
        turno_clase, conflicto = result

        if conflicto:
            return {"error": "El alumno ya está inscrito en una clase con este turno"}

        cursor.execute(
            "INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipo) VALUES (%s, %s, %s)",
            (id_clase, ci_alumno, id_equipo)
        )
        connection.commit()

    except Exception as e:
        return {"error": f"Error al agregar el alumno: {e}"}
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return {"message": "Alumno agregado exitosamente"}


def remove_alumno_de_clase(ci_alumno, id_clase):
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM alumno_clase WHERE ci_alumno = %s AND id_clase = %s",
            (ci_alumno, id_clase))
        connection.commit()

        if cursor.rowcount == 0:
            return {"error": "No se encontró el alumno en la clase especificada"}

    except Exception as e:
        return {"error": f"Error al remover el alumno: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"message": "Alumno removido exitosamente"}
