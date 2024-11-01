from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='proyecto-final',
            user='admin',
            password='admin'
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


@app.route('/login', methods=['GET'])
def get_logins():
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM login")
    logins = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(logins)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
