from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from models import Book
from typing import Optional
from pydantic import BaseModel

Base.metadata.create_all(engine)

app = FastAPI(title="Book collection API")

#home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Collection API"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class Book_Base (BaseModel):
    title: str
    author: str
    year: Optional[int] = None

class Book_Add (Book_Base):
    pass

class Book_Read (Book_Base):
    id: int

    class Config:
        orm_mode = True

#add a new book
@app.post ("/books/", response_model = Book_Read)
def add_book (item: Book_Add, db: Session = Depends(get_db)):
    db_book = Book (title = item.title, author = item.author, year = item.year)
    if not item.title.strip() or not item.author.strip():
        raise HTTPException(status_code=400, detail="Title and author cannot be empty")
    db.add (db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

#get all books
@app.get("/books/", response_model = list[Book_Read])
def read_books (skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Book).offset(skip).limit(limit).all()

#delete a book by id
@app.delete("/books/{book_id}", response_model=dict)
def delete_book (book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException (status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted succesfully"}

#update book details
@app.put("/books/{book_id}", response_model = Book_Read)
def update_book (book_id: int, item: Book_Add, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException (status_code=404, detail="Book not found")
    db_book.title = item.title
    db_book.author = item.author
    db_book.year = item.year

    db.commit()
    db.refresh(db_book)
    return db_book

#search book by author, title or year
@app.get("/books/search/", response_model = list[Book_Read])
def search_books (title: Optional[str] = None,
                  author: Optional[str] = None,
                  year: Optional[int] = None,
                  skip: int = 0, limit: int = 10,
                  db: Session = Depends(get_db)):
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.like(f"%{title}%"))
    if author:
        query = query.filter(Book.author.like(f"%{author}%"))
    if year:
        query = query.filter(Book.year == year)
    return query.offset(skip).limit(limit).all()