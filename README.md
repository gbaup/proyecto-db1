# Proyecto Python

Este proyecto utiliza una estructura basada en `create_app()` para inicializar y ejecutar la aplicación. A continuación,
se explican los pasos para ejecutar el proyecto en diferentes sistemas operativos.

## Requisitos previos

Asegúrate de tener instalado lo siguiente antes de comenzar:

- Python 3.6 o superior
- pip (administrador de paquetes de Python)
- Virtualenv (opcional pero recomendado)

## Configuración inicial

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-repositorio>
    ```

2. Crea y activa un entorno virtual para instalar las dependencias (opcional pero recomendado):

- Mac/Linux:
   ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

- Windows:
   ```bash
  python -m venv venv
  .\venv\Scripts\activate
   ```

3. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt

## Cómo ejecutar el proyecto

1. Navegar hasta el directorio raíz del proyecto.

2. Inicializar docker-compose: se va a crear una base de datos MySQL con datos básicos/iniciales. Estos datos se pueden
   ver y modificar en los archivos 'init.sql' y 'init_data.sql'.

    ```bash
    docker-compose up -d
    ```

3. Inicializar el entorno virtual (si no lo has hecho anteriormente):

- Mac/Linux:
   ```bash
    source venv/bin/activate
    ```

- Windows:
   ```bash
    .\venv\Scripts\activate
    ```

4. Ejecutar el siguiente comando para iniciar la aplicación:

    ```bash
    python main.py
    ```

## Endpoints

El proyecto corre por defecto en el puerto 5000 (configurable). A continuación, se listan los endpoints disponibles:

### Actividades

- GET /actividades
    - Obtiene todas las actividades.
- PUT /actividades/{id}
    - Modifica una actividad (requiere descripcion y costo en el body).

### Alumnos

- POST /alumnos
    - Crea un alumno (requiere nombre, apellido, fecha_nacimiento, mail, telefono en el body).
- PUT /alumnos/{ci}
    - Modifica un alumno (mismo body que el anterior).
- DELETE /alumnos/{ci}
    - Elimina un alumno.

### Clases

- POST /clases
    - Crea una clase (requiere ci_instructor, id_actividad, id_turno en el body).
- PUT /clases/{id}
    - Modifica una clase (requiere ci_instructor, id_turno en el body).
- POST /clases/nuevoalumno
    - Agrega un alumno a una clase (requiere ci_alumno, id_clase, id_equipo en el body).
- DELETE /clases/borraralumno
    - Elimina un alumno de una clase (requiere ci_alumno, id_clase en el body).

### Instructores

- POST /instructor
    - Crea un instructor (requiere ci, nombre, apellido en el body).
- PUT /instructor
    - Modifica un instructor (mismo body que el anterior).
- DELETE /instructor/{id}
    - Elimina un instructor.

### Turnos

- GET /turnos
    - Obtiene todos los turnos.
- POST /turnos
    - Crea un turno (requiere hora_inicio, hora_fin en el body).
- PUT /turnos/{id}
    - Modifica un turno (mismo body que el anterior).
- DELETE /turnos/{id}
    - Elimina un turno.

### Métricas

- GET /metricas/clasemasconcurrida
    - Obtiene la clase más concurrida.
- GET /metricas/clasemasrentable
    - Obtiene la clase más rentable.
- GET /metricas/turnomaspopular
    - Obtiene el turno más popular.



