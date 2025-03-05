from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.session import get_db
from app.models.author import Author as AuthorModel
from app.models.book import Book as BookModel
from app.schemas.author import Author, AuthorCreate, AuthorDetail
from app.schemas.book import Book, BookCreate, BookDetail

# Create API router
router = APIRouter()


# Author endpoints - To be implemented during the test
@router.get("/authors", response_model=List[Author], tags=["authors"])
def list_authors(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """List all authors."""
    # To be implemented during the test
    pass


@router.get("/authors/{author_id}", response_model=AuthorDetail, tags=["authors"])
def get_author(
    author_id: int, 
    db: Session = Depends(get_db)
):
    """Get a specific author by ID."""
    # To be implemented during the test
    pass


@router.post("/authors", response_model=Author, status_code=status.HTTP_201_CREATED, tags=["authors"])
def create_author(
    author: AuthorCreate, 
    db: Session = Depends(get_db)
):
    """Create a new author."""
    # To be implemented during the test
    pass


# Book endpoints - To be implemented during the test
@router.get("/books", response_model=List[Book], tags=["books"])
def list_books(
    skip: int = 0, 
    limit: int = 100, 
    author_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """List all books with optional filtering by author."""
    # To be implemented during the test
    pass


@router.get("/books/{book_id}", response_model=BookDetail, tags=["books"])
def get_book(
    book_id: int, 
    db: Session = Depends(get_db)
):
    """Get a specific book by ID."""
    # To be implemented during the test
    pass


@router.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED, tags=["books"])
def create_book(
    book: BookCreate, 
    db: Session = Depends(get_db)
):
    """Create a new book."""
    # To be implemented during the test
    pass