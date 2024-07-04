from sqlalchemy.orm import Session

from schemas.character import CharacterSchema
from models.character import Character


# Función para obtener todos los personajes
def get_characters(db: Session):
    return db.query(Character).all()


# Función para obtener un personaje por su ID
def get_character(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()


# Función para crear un nuevo personaje
def create_character(db: Session, character: CharacterSchema):
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


# Función para eliminar un personaje por su ID
def delete_character(db: Session, character_id: int):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if db_character:
        db.delete(db_character)
        db.commit()
        return db_character
    return None
