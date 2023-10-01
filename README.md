# My FastAPI Article Management App

## Overview
This is a FastAPI-based web application for managing articles. It provides a REST API for creating, retrieving, updating, and deleting articles.

## Project Structure
- `app/` - Contains the application code.
    - `main.py` - FastAPI application setup and routes.
    - `business_logic.py` - Business logic layer.
    - `controller.py` - Controller (routes) for the API.
    - `data_access.py` - Data access layer with SQLAlchemy.
    - `models.py` - SQLAlchemy models for the database.

## Getting Started
1. Install the required dependencies listed in `requirements.txt`.
2. Configure your database connection in `app/main.py`.
3. Run the FastAPI application: `uvicorn app.main:app --reload`.

## API Documentation
- `/articles` - POST: Create a new article.
- `/articles/` - GET: Get a list of all articles. (Cached with LRU mechanism for improved performance)
- `/articles/{article_id}` - GET: Get a specific article by ID.
- `/articles/{article_id}` - PUT: Update an article by ID.
- `/articles/{article_id}` - DELETE: Delete an article by ID.

## Caching
The `/articles/` endpoint is cached using an LRU (Least Recently Used) cache mechanism for improved performance. The list of articles is cached and retrieved from the cache for subsequent requests, reducing the need for repeated database queries.

## Author
Fadi Zaboura
