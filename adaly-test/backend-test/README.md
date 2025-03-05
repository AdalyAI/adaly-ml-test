# Backend Developer Test - Library API

This repository contains a starter template for the backend developer technical test. Your task is to implement a Library API using FastAPI and Alembic for database migrations.

## Setup Instructions

1. Clone this repository

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on the `.env.example` template

5. Initialize the database:
   ```bash
   alembic upgrade head
   ```

6. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

7. Access the API documentation at http://localhost:8000/docs

## Project Structure

```
backend-test/
├── app/                    # Application package
│   ├── api/                # API endpoints
│   ├── core/               # Core configuration
│   ├── db/                 # Database setup
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic models
│   └── main.py             # FastAPI application
├── migrations/             # Alembic migrations
│   ├── versions/           # Migration versions
│   ├── env.py              # Alembic environment
│   └── alembic.ini         # Alembic configuration
├── tests/                  # Test directory
├── .env.example            # Environment variables example
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
```

## Development Tasks

Please refer to the test document for specific tasks to complete.

## Submission

When you've completed the test or the time is up:

1. Make sure all your code is committed
2. Update this README with any additional information
3. Ensure your code runs with the provided instructions