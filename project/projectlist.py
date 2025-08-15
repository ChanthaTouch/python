from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from projectlistmodel import Projectlist
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# Pydantic Schemas
# =========================
class ProjectlistBase(BaseModel):
    client_name: str
    project_name: str
    start_date: str
    end_date: str
    location: str
    budget: str
    min_labour: str
    variant_extra_OT: str
    team_OT_limit: str

class ProjectlistCreate(ProjectlistBase):
    pass

class ProjectlistUpdate(ProjectlistBase):
    pass

class ProjectlistResponse(ProjectlistBase):
    id: int
    class Config:
        from_attributes = True  # Pydantic v2

# =========================
# CRUD Endpoints
# =========================

@app.post("/projects", response_model=ProjectlistResponse)
def create_project(project: ProjectlistCreate, db: Session = Depends(get_db)):
    new_project = Projectlist(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@app.get("/projects", response_model=List[ProjectlistResponse])
def get_all_projects(db: Session = Depends(get_db)):
    return db.query(Projectlist).all()

@app.get("/projects/{project_id}", response_model=ProjectlistResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Projectlist).filter(Projectlist.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.put("/projects/{project_id}", response_model=ProjectlistResponse)
def update_project(project_id: int, updated: ProjectlistUpdate, db: Session = Depends(get_db)):
    project = db.query(Projectlist).filter(Projectlist.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    for key, value in updated.dict().items():
        setattr(project, key, value)
    
    db.commit()
    db.refresh(project)
    return project

@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Projectlist).filter(Projectlist.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}
