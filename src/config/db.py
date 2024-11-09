# src/config/db.py
import mysql.connector
from mysql.connector import Error
from src.config import DB_CONFIG


def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
