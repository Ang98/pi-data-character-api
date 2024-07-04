# Character API

Este proyecto implementa una API para gestionar datos de personajes (`characters`) utilizando FastAPI y SQLAlchemy. Permite realizar operaciones CRUD básicas sobre estos datos.

## APIs del Proyecto

### 1. Obtener todos los personajes

- **Descripción**: Retorna una lista con todos los personajes almacenados.
- **Método HTTP**: GET
- **Ruta**: `/character/getAll`

### 2. Obtener un personaje por ID

- **Descripción**: Retorna los detalles de un personaje específico identificado por su ID.
- **Método HTTP**: GET
- **Ruta**: `/character/get/{id}`

### 3. Crear un nuevo personaje

- **Descripción**: Crea un nuevo personaje con la información proporcionada.
- **Método HTTP**: POST
- **Ruta**: `/character/add`

### 4. Eliminar un personaje por ID

- **Descripción**: Elimina un personaje específico identificado por su ID.
- **Método HTTP**: DELETE
- **Ruta**: `/character/delete/{id}`

## Estructura del Proyecto

El proyecto sigue una estructura organizativa basada en Clean Architecture para mantener una separación clara de las capas y responsabilidades:

  - **`main.py`**: Punto de entrada de la aplicación FastAPI que configura y arranca la aplicación.
  - **`crud/`**: Funciones CRUD para interactuar con la base de datos.
  - **`models/`**: Definiciones de modelos SQLAlchemy que representan las tablas de la base de datos.
  - **`schemas/`**: Esquemas Pydantic para validar datos de entrada y salida de la API.
  - **`services/`**: Lógica de negocio y servicios.

- **`databases/`**: Configuración de la base de datos y sesiones SQLAlchemy.

- **`tests/`**: Directorio opcional para pruebas unitarias.

## Comandos para Ejecutar el Proyecto

### Ejecución Local

1. **Instalar dependencias:**

   ```bash
   #Crear entorno virtual
   python -m venv .venv

   #Activar entorno virtual
   source .venv/bin/activate

   #Instalar dependencias
   pip install -r requirements.txt

   #Correr aplicacion
   uvicorn main:app --reload
   

### Ejecución con Docker

1. **Instalar dependencias:**

   ```bash
   docker compose up


## Documentacion de codigo

La documentacino de codigo se encuentra en la ruta:  [http://localhost:8000/docs](http://localhost:8000/docs).
