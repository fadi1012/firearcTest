from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.business_layer import BusinessLogicLayer
from app.main import app
from app.models import Article


# Dependency to get the database session
def get_db() -> Session:
    return app.state.db


@app.get("/articles/", response_model=List[Article],
         response_description="Returns list of articles in DB",
         responses={404: {'model': str, 'description': 'Articles not found'}}
         )
def get_all_articles(db: Session = Depends(get_db)):
    return BusinessLogicLayer.get_all_articles(db)


@app.get("/articles/{article_id}", response_model=Article,
         response_description="Returns specific article by ID from DB",
         responses={404: {'model': str, 'description': 'Article not found'}}
         )
def get_article_by_id(article_id: int, db: Session = Depends(get_db)):
    article = BusinessLogicLayer.get_article_by_id(db, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@app.put("/articles/{article_id}", response_model=Article,
         response_description="Updates article details",
         responses={404: {'model': str, 'description': 'Article not found'}}
         )
def update_article_by_id(article_id: int, updated_article: Article, db: Session = Depends(get_db)):
    article = BusinessLogicLayer.update_article_by_id(db, article_id, updated_article)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@app.delete("/articles/{article_id}", response_model=bool,
            response_description="Deletes article by ID",
            responses={404: {'model': str, 'description': 'Article not found'}}
            )
def delete_article_by_id(article_id: int, db: Session = Depends(get_db)):
    success = BusinessLogicLayer.delete_article_by_id(db, article_id)
    if not success:
        raise HTTPException(status_code=404, detail="Article not found")
    return True
