from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from schemas.character import CharacterSchema

from services.crud_character import get_character, create_character, delete_character, get_characters
from models.character import Base
from databases.database import SessionLocal, engine


# Crea las tablas en la base de datos utilizando metadata y el motor de SQLAlchemy
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():

    # Crea una instancia de SessionLocal para la base de datos
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Ruta para obtener todos los personajes
@app.get("/character/getAll", response_model=list[CharacterSchema])
def read_characters_api(db: Session = Depends(get_db)):
    characters = get_characters(db)
    return characters


# Ruta para obtener un personaje por su ID
@app.get("/character/get/{id}", response_model=CharacterSchema)
def read_character_api(id: int, db: Session = Depends(get_db)):
    character = get_character(db, id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


# Ruta para crear un nuevo personaje
@app.post("/character/add", response_model=CharacterSchema)
def create_character_api(character: CharacterSchema, db: Session = Depends(get_db)):
    existing_character = get_character(db, character.dict().get("id"))
    if existing_character:
        raise HTTPException(status_code=400, detail="Character already exists")
    return create_character(db=db, character=character)


# Ruta para eliminar un personaje por su ID
@app.delete("/character/delete/{id}", response_model=CharacterSchema)
def delete_character_api(id: int, db: Session = Depends(get_db)):
    character = delete_character(db, id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character
