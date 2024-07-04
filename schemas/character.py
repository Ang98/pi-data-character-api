from pydantic import BaseModel

# Definición de un esquema Pydantic para la base de datos de personajes
class CharacterBaseSchema(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int


# Esquema extendido que incluye el ID del personaje para la respuesta de la API
class CharacterSchema(CharacterBaseSchema):
    id: int

    class Config:
        # Configuración para habilitar el modo ORM de Pydantic
        orm_mode = True
