from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from view.database import SessionLocal
from clientmodel import Client
from view.schemas import ClientCreate, ClientUpdate
from typing import List

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Client
@app.post("/clients", response_model=ClientCreate)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = Client(
        project_name=client.project_name,
        address=client.address,
        phone=client.phone,
        email=client.email,
        website=client.website
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

# Read All Clients
@app.get("/clients", response_model=List[ClientCreate])
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()

# Read Client by ID
@app.get("/clients/{client_id}", response_model=ClientCreate)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# Update Client
@app.put("/clients/{client_id}", response_model=ClientCreate)
def update_client(client_id: int, updated_client: ClientUpdate, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    client.project_name = updated_client.project_name
    client.address = updated_client.address
    client.phone = updated_client.phone
    client.email = updated_client.email
    client.website = updated_client.website

    db.commit()
    db.refresh(client)
    return client

# Delete Client
@app.delete("/clients/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    db.delete(client)
    db.commit()
    return {"message": "Client deleted successfully"}
