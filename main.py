from fastapi import FastAPI, HTTPException, Depends
from modules import database, models, schemas
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/requisitos/", response_model=schemas.Requisito)
def create_requisito(requisito: schemas.RequisitoCreate, db: Session = Depends(get_db)):
    db_requisito = models.Requisito(titulo=requisito.titulo, descricao=requisito.descricao)
    db.add(db_requisito)
    db.commit()
    db.refresh(db_requisito)
    return db_requisito
@app.get("/requisitos/", response_model=List[schemas.Requisito])
def read_requisitos(db: Session = Depends(get_db)):
    requisitos = db.query(models.Requisito).all()
    return requisitos
@app.get("/requisitos/{requisito_id}", response_model=schemas.Requisito)
def read_requisito(requisito_id: int, db: Session = Depends(get_db)):
    requisito = db.query(models.Requisito).filter(models.Requisito.id == requisito_id).first()
    if requisito is None:
        raise HTTPException(status_code=404, detail="Requisito not found")
    return requisito
@app.put("/requisitos/{requisito_id}", response_model=schemas.Requisito)
def update_requisito(requisito_id: int, requisito: schemas.RequisitoUpdate, db: Session = Depends(get_db)):
    db_requisito = db.query(models.Requisito).filter(models.Requisito.id == requisito_id).first()
    if db_requisito is None:
        raise HTTPException(status_code=404, detail="Requisito not found")
    db_requisito.titulo = requisito.titulo
    db_requisito.descricao = requisito.descricao
    db.commit()
    db.refresh(db_requisito)
    return db_requisito
@app.delete("/requisitos/{requisito_id}", response_model=schemas.Requisito)
def delete_requisito(requisito_id: int, db: Session = Depends(get_db)):
    db_requisito = db.query(models.Requisito).filter(models.Requisito.id == requisito_id).first()
    if db_requisito is None:
        raise HTTPException(status_code=404, detail="Requisito not found")
    db.delete(db_requisito)
    db.commit()
    return db_requisito