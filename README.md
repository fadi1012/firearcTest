
# My FastAPI Article Management App

## Overview
This is a FastAPI-based web application for managing articles. It provides a REST API for creating, retrieving, updating, and deleting articles.

## Project Structure
- `app/` - Contains the application code.
    - `main.py` - FastAPI application setup and routes.
    - `business_logic.py` - Business logic layer.
    - `controller.py` - Controller (routes) for the API.
    - `data_access.py` - Data access layer with aiosqlite.
    - `models.py` - Pydantic data models for the API.

## Getting Started
1. Install the required dependencies listed in `requirements.txt`.

2. Run the FastAPI application using Uvicorn:

```bash
uvicorn app.main:app --reload
```

3. Alternatively, you can use Docker to run the application:

## Using Docker

Ensure you have Docker installed on your system.

### Build the Docker Image

Navigate to the project directory containing the Dockerfile and run:

```bash
docker build -t fastapi-article-app .
```

### Run the Docker Container

After successfully building the Docker image, you can run the application in a Docker container:

```bash
docker run -p 8000:8000 fastapi-article-app
```

The FastAPI application will be accessible at `http://localhost:8000` in your web browser or API client.

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