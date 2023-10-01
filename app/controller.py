from typing import List
import aiosqlite
from fastapi import Depends

from app.business_layer import BusinessLogicLayer
from app.main import app
from app.models import Article
from cachetools import LRUCache, cached


# Dependency to get the database connection
def get_db() -> aiosqlite.Connection:
    return app.state.db


# Define an LRU cache with a maximum size
article_cache = LRUCache(maxsize=100)


def clear_cache():
    article_cache.clear()

def cached_article(func):
    return cached(article_cache, key=lambda db, article_id: article_id)(func)


@cached_article  # Cache the result of this function
@app.get("/articles/", response_model=List[Article],
         response_description="Returns list of articles in DB",
         responses={404: {'model': str, 'description': 'Articles not found'}}
         )
async def get_all_articles(db: aiosqlite.Connection = Depends(get_db)):
    return BusinessLogicLayer.get_all_articles(db)


@app.get("/articles/{article_id}", response_model=Article,
         response_description="Returns specific article by ID from DB",
         responses={404: {'model': str, 'description': 'Article not found'}}
         )
async def get_article_by_id(article_id: int, db: aiosqlite.Connection = Depends(get_db)):
    return BusinessLogicLayer.get_article_by_id(article_id=article_id, db=db)


@app.put("/articles/{article_id}", response_model=Article,
         response_description="Updates article details",
         responses={404: {'model': str, 'description': 'Article not found'}}
         )
async def update_article_by_id(article_id: int, updated_article: Article, db: aiosqlite.Connection = Depends(get_db)):
    return BusinessLogicLayer.update_article_by_id(article_id=article_id, updated_article=updated_article, db=db)


@app.delete("/articles/{article_id}", response_model=bool,
            response_description="Deletes article by ID",
            responses={404: {'model': str, 'description': 'Article not found'}}
            )
async def delete_article_by_id(article_id: int, db: aiosqlite.Connection = Depends(get_db)):
    return BusinessLogicLayer.delete_article_by_id(article_id=article_id, db=db)


@app.post("/articles", response_model=Article)
async def create_article(article: Article, db: aiosqlite.Connection = Depends(get_db)):
    return BusinessLogicLayer.create_article(article, db)
