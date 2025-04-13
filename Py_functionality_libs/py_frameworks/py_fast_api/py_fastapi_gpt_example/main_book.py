from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory "database"
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
]

# Schema for input validation
class Book(BaseModel):
    title: str
    author: str

@app.get("/books", response_model=List[dict])
def get_books(search: Optional[str] = None):
    if search:
        return [book for book in books if search.lower() in book["title"].lower()]
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", status_code=201)
def add_book(book: Book):
    new_id = max([b["id"] for b in books], default=0) + 1
    new_book = {"id": new_id, "title": book.title, "author": book.author}
    books.append(new_book)
    return new_book

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    global books
    books = [book for book in books if book["id"] != book_id]
    return