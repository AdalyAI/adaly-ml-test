# Backend Developer Technical Test
**Duration: 1 Hour**

## Overview

This test evaluates your proficiency with FastAPI and Alembic for building and maintaining backend services. You'll build a simple API for managing a library of books with proper database migrations.

## Prerequisites

- Python 3.8+
- Git
- SQL basics
- Understanding of RESTful APIs

## Setup Instructions

1. Clone the test repository:
   ```
   git clone https://github.com/AdalyAI/adaly-ml-test
   cd adaly-ml-test
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Task 1: Database Schema and Migrations (15 minutes)

Using Alembic, create the necessary migration files for the following data models:

1. `Author` model with fields:
   - id (integer, primary key)
   - name (string, not null)
   - biography (text, nullable)
   - date_of_birth (date, nullable)

2. `Book` model with fields:
   - id (integer, primary key)
   - title (string, not null)
   - description (text, nullable)
   - publication_date (date, nullable)
   - author_id (foreign key to Author)

Implement the SQLAlchemy models and create the initial Alembic migration to set up these tables.

## Task 2: FastAPI Endpoints (20 minutes)

Create a FastAPI application with the following endpoints:

1. `GET /authors` - List all authors
2. `GET /authors/{author_id}` - Get details of a specific author
3. `POST /authors` - Create a new author
4. `GET /books` - List all books (with optional query parameter to filter by author)
5. `GET /books/{book_id}` - Get details of a specific book
6. `POST /books` - Create a new book

Requirements:
- Implement proper request/response models using Pydantic
- Include appropriate status codes and error handling
- Include proper documentation using FastAPI's built-in features

## Task 3: Database Migration Modifications (15 minutes)

Create a new Alembic migration that adds the following to your database schema:

1. Add a `genre` field (string, nullable) to the `Book` model
2. Add a `unique` constraint on the book `title` field
3. Create an index on the `author_id` field in the `Book` table

Ensure the migration can be applied and reverted cleanly.

## Task 4: Advanced FastAPI Features (10 minutes)

Implement any two of the following FastAPI features:

1. Add pagination to the `GET /books` endpoint
2. Implement a dependency for database session management
3. Add rate limiting to the API endpoints
4. Implement a custom middleware to log request details

## Bonus (if time permits):

- Add unit tests for at least two endpoints
- Implement a bulk import endpoint for books
- Add a simple search functionality for books by title or author name

## Submission

When you've completed the test or the time is up:

1. Make sure all your code is committed to Git
2. Provide a brief README explaining your implementation choices
3. Include instructions on how to run your application and apply migrations

## Evaluation Criteria

- **Code quality**: Clean, well-structured, and readable code
- **FastAPI knowledge**: Proper use of FastAPI features and patterns
- **Database handling**: Correct implementation of models and migrations
- **Error handling**: Graceful handling of edge cases and errors
- **Documentation**: Clear API documentation and code comments
