from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from view.database import SessionLocal
from view.models import Book
from view.schemas import BookCreate, BookUpdate, BookResponse
from typing import List

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all books
@app.get("/books", response_model=List[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

# Get book by ID
@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Create new book
@app.post("/books", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(title=book.title, author=book.author, price=book.price)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Update book by ID
@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, updated_book: BookUpdate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = updated_book.title
    book.author = updated_book.author
    book.price = updated_book.price
    db.commit()
    db.refresh(book)
    return book

# Delete book by ID
@app.delete("/books/{book_id}", response_model=BookResponse)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return book
