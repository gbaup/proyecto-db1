from src.config.db import get_db_connection


def get_clase_mas_concurrida():
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id_clase, COUNT(ci_alumno) AS cantidad_alumnos FROM alumno_clase GROUP BY id_clase ORDER BY cantidad_alumnos DESC LIMIT 1"
        )
        result = cursor.fetchone()

        if result is None:
            return {"error": "No se encontraron clases"}

    except Exception as e:
        return {"error": f"Error al obtener la clase más concurrida: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"id_clase": result[0], "cantidad_alumnos": result[1]}


def get_clase_mas_rentable():
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                ac.id_clase,
                SUM(a.costo + e.costo) AS ingresos_totales
            FROM
                alumno_clase ac
            JOIN
                clase c ON ac.id_clase = c.id
            JOIN
                actividades a ON c.id_actividad = a.id
            JOIN
                equipamiento e ON ac.id_equipo = e.id
            GROUP BY
                ac.id_clase
            ORDER BY
                ingresos_totales DESC
            LIMIT 1;
            """
        )
        result = cursor.fetchone()

        if result is None:
            return {"error": "No se encontraron clases"}

    except Exception as e:
        return {"error": f"Error al obtener la clase más rentable: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"id_clase": result[0], "ingresos": result[1]}


def get_turno_mas_popular():
    connection = get_db_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                c.id_turno,
                COUNT(c.id) AS cantidad_clases
            FROM
                clase c
            WHERE
                c.dictada = 1
            GROUP BY
                c.id_turno
            ORDER BY
                cantidad_clases DESC
            LIMIT 1;
            """
        )
        result = cursor.fetchone()

        if result is None:
            return {"error": "No se encontraron turnos"}

    except Exception as e:
        return {"error": f"Error al obtener el turno más popular: {e}"}
    finally:
        cursor.close()
        connection.close()

    return {"id_turno": result[0], "cantidad_alumnos": result[1]}
