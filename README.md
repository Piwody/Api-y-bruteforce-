# Proyecto FastAPI - CRUD de Usuarios + Ataque de Fuerza Bruta

## Descripción
Este proyecto nos ayuda a compredner el uso de las API y de un Bruteforce contra una interfaz de progrmacion, y el objetivo es medir el tiempo que tarda en econtrar y que tan eficaz son nuestras contrasenas 
## Estructura

/api: Contiene el servidor desarrollado con FastAPI y SQLModel.
/ataque: Contiene el script autonomo.py que realiza el intento de intrusión.

## Requisitos
- Python
- Entorno virtual (venv)
- Dependencias del archivo requirements.txt

## Instalación

1. Crear entorno virtual:
python -m venv venv

2. Activar entorno virtual:
venv\Scripts\activate

3. Instalar dependencias en mi caso:
 Python pip install -r requirements.txt

## Ejecución de la API

Ejecutar el servidor FastAPI:
fastapi dev main.py

Abrir en el navegador:
http://127.0.0.1:8000/docs

## Ejemplo de Login

POST /login
{
"username": "admin",
"password": "admin1"
}

Respuesta:
{
"message": "Exitoso"
}

## Ejecución del ataque de fuerza bruta

Se abre una nueva terminal (con la API corriendo) y ejecutamos lo siguiente:

python attack.py

## Funcion del ataque

El script autonomo.py realiza lo siguiente:

-Utiliza la librería itertools para realizar una búsqueda exhaustiva:

-El script no usa un diccionario estático, sino que genera combinaciones matemáticas basadas en un alfabeto definido.

-Envía cada clave generada mediante el método POST al endpoint /login.

Análisis de Respuesta:

Si recibe un código 401 (Unauthorized), el ataque continúa con la siguiente combinación.

Si recibe un código 200 (OK), el ataque se detiene y reporta el éxito.

## Ejemplo de Salida 
{'clave': 'pass1', 'intentos': 1371, 'tiempo': 28.360916 segundos}

Si no encuentra la clave:
{'clave': None, 'intentos': 47988, 'tiempo': 629.510406 segundos }

## Importante 
Se utilizó el nombre de variable pana en el código para representar al usuario objetivo.

Se implementó el manejo de errores try/except para evitar que el script colapse ante fallos de conexión.
