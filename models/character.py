from sqlalchemy import Column, Integer, String
from databases.database import Base

# Define una clase Character que hereda de Base, que es la clase base de SQLAlchemy para declaraciones
class Character(Base):

    # Nombre de la tabla en la base de datos
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(Integer)
