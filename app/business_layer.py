import aiosqlite
from fastapi import Depends

from app.main import get_db
from app.models import Article
from app.data_access import DataAccessLayer


class BusinessLogicLayer:
    @classmethod
    def get_all_articles(cls, db: aiosqlite.Connection = Depends(get_db)) -> list[Article]:
        return DataAccessLayer.get_all_articles(db=db)

    @classmethod
    def get_article_by_id(cls, article_id: int, db: aiosqlite.Connection = Depends(get_db)) -> Article:
        return DataAccessLayer.get_article_by_id(article_id=article_id, db=db)

    @classmethod
    def update_article_by_id(cls, article_id: int, updated_article: Article,
                             db: aiosqlite.Connection = Depends(get_db)) -> Article:
        return DataAccessLayer.update_article_by_id(article_id=article_id, updated_article=updated_article, db=db)

    @classmethod
    def delete_article_by_id(cls, article_id: int, db: aiosqlite.Connection = Depends(get_db)) -> bool:
        return DataAccessLayer.delete_article_by_id(article_id=article_id, db=db)

    @classmethod
    def create_article(cls, new_article: Article, db: aiosqlite.Connection = Depends(get_db)) -> list[Article]:
        return DataAccessLayer.create_article(article=new_article, db=db)
