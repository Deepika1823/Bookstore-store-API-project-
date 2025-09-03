📚 Bookstore REST API

A simple REST API built with FastAPI + SQLite + SQLAlchemy, for managing a bookstore inventory.
Supports full CRUD operations, search/filtering, and works with Postman for testing.

🚀 Features

Add new books 📖

View all books or a single book 🔎

Update book details ✏️

Delete books ❌

SQLite database with SQLAlchemy ORM

Swagger UI documentation (auto-generated)

🛠️ Tech Stack

Python 3.12+

FastAPI (API framework)

SQLAlchemy (ORM)

SQLite (database)

Pydantic (data validation)

Postman (API testing)

📂 Project Structure
internship project/
│── main.py                  # FastAPI app
│── books.db                 # SQLite database file
│── Bookstore_API.postman_collection.json   # Postman collection
│── README.md                 # Project documentation

⚙️ Setup & Run

Clone or download the project.

Install dependencies:

pip install fastapi uvicorn sqlalchemy pydantic


Run the FastAPI server:

uvicorn main:app --reload


Open in browser:

API Docs: 👉 http://127.0.0.1:8000/docs

API Root: 👉 http://127.0.0.1:8000/

📌 API Endpoints
1. Root

GET /
→ Welcome message

2. Create Book

POST /books/

{
  "title": "Book Title",
  "author": "Author Name",
  "price": 250.0,
  "quantity": 10
}

3. Get All Books

GET /books/

4. Get Book by ID

GET /books/{book_id}

5. Update Book

PUT /books/{book_id}

6. Delete Book

DELETE /books/{book_id}

🧪 Testing with Postman

Open Postman.

Click Import → Upload File.

Select Bookstore_API.postman_collection.json.

Test all endpoints easily.

🗄️ Database

SQLite file: books.db

Table: books

id INTEGER PRIMARY KEY,
title TEXT,
author TEXT,
price REAL,
quantity INTEGER

📖 Future Improvements

User authentication 🔑

Pagination & sorting

Deploy to cloud (Heroku, Render, etc.)