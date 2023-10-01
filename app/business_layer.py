from sqlalchemy.orm import Session
from app.models import Article
from app.data_access import DataAccessLayer


class BusinessLogicLayer:
    @classmethod
    def get_all_articles(cls, db: Session) -> list[Article]:
        return DataAccessLayer.get_all_articles(db)

    @classmethod
    def get_article_by_id(cls, db: Session, article_id: int) -> Article:
        return DataAccessLayer.get_article_by_id(db, article_id)

    @classmethod
    def update_article_by_id(cls, db: Session, article_id: int, updated_article: Article) -> Article:
        return DataAccessLayer.update_article_by_id(db, article_id, updated_article)

    @classmethod
    def delete_article_by_id(cls, db: Session, article_id: int) -> bool:
        return DataAccessLayer.delete_article_by_id(db, article_id)
