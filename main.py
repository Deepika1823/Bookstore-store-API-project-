from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# -----------------------------
# Database setup
# -----------------------------
DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)


# Create tables
Base.metadata.create_all(bind=engine)

# -----------------------------
# Pydantic Schema
# -----------------------------
class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    quantity: int

    class Config:
        from_attributes = True  # replaces orm_mode in Pydantic v2


# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(title="📚 Bookstore API")


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# Root route (welcome)
# -----------------------------
@app.get("/")
def root():
    return {"message": "📚 Bookstore API is running 🚀"}


# -----------------------------
# CRUD Routes
# -----------------------------
@app.post("/books/", response_model=BookCreate)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=list[BookCreate])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@app.get("/books/{book_id}", response_model=BookCreate)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=BookCreate)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": f"Book with ID {book_id} deleted successfully"}
