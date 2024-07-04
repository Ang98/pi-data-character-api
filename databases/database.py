import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Obtener la URL de la base de datos desde las variables de entorno
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

# Crear el motor de SQLAlchemy con la URL de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear una sesión de SQLAlchemy que será utilizada por el ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear una clase base para las clases declarativas de SQLAlchemy
Base = declarative_base()
