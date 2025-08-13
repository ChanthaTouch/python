from fastapi import FastAPI, Body, HTTPException

app = FastAPI()

# Book database with IDs
BOOKS = [
    {"id": 1, "title": "Love Him Alone", "author": "Touch Chantha", "price": "30000r"},
    {"id": 2, "title": "Him Love Her", "author": "Touch Chantha", "price": "25000r"},
    {"id": 3, "title": "Thinking of Life", "author": "Chan Sery", "price": "25000r"},
    {"id": 4, "title": "Sunset Dreams", "author": "Sok Dara", "price": "20000r"},
    {"id": 5, "title": "Moonlight Tales", "author": "Chan Sery", "price": "30000r"},
    {"id": 6, "title": "Journey Within", "author": "Touch Chantha", "price": "35000r"},
    {"id": 7, "title": "Whispers of Time", "author": "Sok Dara", "price": "28000r"},
    {"id": 8, "title": "Paths of Hope", "author": "Khim Sovann", "price": "22000r"},
    {"id": 9, "title": "Silent Waves", "author": "Chan Sery", "price": "27000r"}
]

# Get all books
@app.get('/books')
async def get_books():
    return BOOKS

# Get book by ID
@app.get('/books/{book_id}')
async def get_book(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Get books by price
@app.get('/books/price/{price}')
async def get_books_by_price(price: str):
    books_to_return = [book for book in BOOKS if book["price"].casefold() == price.casefold()]
    return books_to_return

# Get books by author and price
@app.get('/books/author/{author}/price/{price}')
async def get_books_by_author_and_price(author: str, price: str):
    books_to_return = [
        book for book in BOOKS
        if book["author"].casefold() == author.casefold() and book["price"].casefold() == price.casefold()
    ]
    return books_to_return

# Create new book
@app.post('/books')
async def create_book(new_book: dict = Body(...)):
    new_id = max([book["id"] for book in BOOKS], default=0) + 1
    new_book["id"] = new_id
    BOOKS.append(new_book)
    return {"message": "Book added successfully", "book": new_book}

# Update book by ID
@app.put('/books/{book_id}')
async def update_book(book_id: int, updated_book: dict = Body(...)):
    for i, book in enumerate(BOOKS):
        if book["id"] == book_id:
            updated_book["id"] = book_id
            BOOKS[i] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}
    raise HTTPException(status_code=404, detail="Book not found")

# Delete book by ID
@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
    for i, book in enumerate(BOOKS):
        if book["id"] == book_id:
            deleted_book = BOOKS.pop(i)
            return {"message": "Book deleted successfully", "book": deleted_book}
    raise HTTPException(status_code=404, detail="Book not found")
